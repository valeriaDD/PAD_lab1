import logging
import threading
import time

import grpc
from flask import Flask, request, abort

from CacheHashRing import CacheHashRing
from CircuitBreaker import CircuitBreaker, RerouteException, CircuitBreakerException
from proto import coordinator_pb2_grpc, coordinator_pb2, service_discovery_pb2_grpc, service_discovery_pb2, scooters_pb2, scooters_pb2_grpc, bookings_pb2_grpc, \
    bookings_pb2

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(name)s | [%(levelname)s]: %(message)s")

SERVICE_DISCOVERY_PORT = 2000
SERVICE_NAME = "service-discovery"

app = Flask(__name__)

semaphore = threading.Semaphore(2)
booking_circuit_breaker = CircuitBreaker()
scooters_circuit_breaker = CircuitBreaker()
coordinator_circuit_breaker = CircuitBreaker()

nodes = {
    'redis_node_1': {'host': 'redis', 'port': 6379},
    'redis_node_2': {'host': 'redis_2', 'port': 6379},
}

redis_hash_ring = CacheHashRing(nodes)

grpc_to_http_status = {
        grpc.StatusCode.OK: 200,
        grpc.StatusCode.UNKNOWN: 500,
        grpc.StatusCode.NOT_FOUND: 404,
        grpc.StatusCode.INTERNAL: 500,
        grpc.StatusCode.INVALID_ARGUMENT: 422,
    }


def get_scooter_service_channel(service_name):
    try:
        with grpc.insecure_channel(f'{SERVICE_NAME}:{SERVICE_DISCOVERY_PORT}') as channel:
            stub = service_discovery_pb2_grpc.ServiceRegistryStub(channel)
            response = stub.DiscoverService(service_discovery_pb2.ServiceRequest(service_name=service_name))
            return grpc.insecure_channel(f"{response.host}:{response.port}")
    except grpc.RpcError as e:
        abort(500, description="Service discovery failed")


@app.route("/")
def hello_world():
    with semaphore:
        time.sleep(3)
        return "hello!!"


@app.route('/book/scooters/<int:scooter_id>', methods=['POST'])
def book_scooter(scooter_id):
    while True:
        with semaphore:
            data = request.json
            request_data = bookings_pb2.BookScooterRequest(
                scooter_id=str(scooter_id),
                start=data['start'],
                user_email=data['user_email'],
                title=data['title']
            )
            try:
                with get_scooter_service_channel("coordinator") as channel:
                    stub = coordinator_pb2_grpc.CoordinatorStub(channel)
                    response = booking_circuit_breaker.call(lambda: stub.BookScooter(request_data, timeout=5.0))

                    redis_hash_ring.delete('all_bookings')
                    return {
                        'id': response.id,
                        'title': response.title,
                        'start': response.start,
                        'user_email': response.user_email,
                        'scooter_id': response.scooter_id,
                        'end': response.end
                    }

            except RerouteException as e:
                continue
            except grpc.RpcError as e:
                abort(grpc_to_http_status.get(e.code(), 500), description=e.details())
            except CircuitBreakerException as e:
                abort(500, description=str(e))


@app.route('/book/<int:booking_id>/end-ride', methods=['PATCH'])
def end_ride(booking_id):
    while True:
        request_data = bookings_pb2.EndRideRequest(id=booking_id)
        try:
            with get_scooter_service_channel("coordinator") as channel:
                stub = coordinator_pb2_grpc.CoordinatorStub(channel)
                response = coordinator_circuit_breaker.call(lambda: stub.EndRide(request_data, timeout=5.0))

                cache_key = f'booking_{booking_id}'
                redis_hash_ring.delete(cache_key)
                redis_hash_ring.delete('all_bookings')
                return {
                    'id': response.id,
                    'title': response.title,
                    'start': response.start,
                    'user_email': response.user_email,
                    'scooter_id': response.scooter_id,
                    'end': response.end
                }
        except RerouteException as e:
            continue
        except grpc.RpcError as e:
            abort(grpc_to_http_status.get(e.code(), 500), description=e.details())

        except CircuitBreakerException as e:
            abort(500, description=str(e))


@app.route('/book/<int:booking_id>', methods=['GET'])
def get_booking(booking_id):
    while True:
        request_data = bookings_pb2.GetBookingRequest(id=booking_id)
        try:
            with get_scooter_service_channel("bookings") as channel:
                stub = bookings_pb2_grpc.BookingsServiceStub(channel)
                response = booking_circuit_breaker.call(lambda: stub.GetBooking(request_data, timeout=5.0))

                booking = {
                    'id': response.id,
                    'title': response.title,
                    'start': response.start,
                    'user_email': response.user_email,
                    'scooter_id': response.scooter_id,
                    'end': response.end
                }
                redis_hash_ring.set(f'booking_{booking_id}', booking)
                return booking
        except RerouteException as e:
            continue
        except grpc.RpcError as e:
            abort(grpc_to_http_status.get(e.code(), 500), description=e.details())

        except CircuitBreakerException as e:
            abort(500, description=str(e))


@app.route('/book', methods=['GET'])
def get_all_bookings():
    while True:
        try:
            with get_scooter_service_channel("bookings") as channel:
                stub = bookings_pb2_grpc.BookingsServiceStub(channel)
                response = booking_circuit_breaker.call(
                    lambda: stub.GetAllBookings(service_discovery_pb2.Empty(), timeout=5.0))

                bookings = [
                    {
                        'id': booking.id,
                        'title': booking.title,
                        'start': booking.start,
                        'user_email': booking.user_email,
                        'scooter_id': booking.scooter_id,
                        'end': booking.end
                    } for booking in response.bookings
                ]

                redis_hash_ring.set('all_bookings', bookings)

                return bookings
        except RerouteException as e:
            continue
        except grpc.RpcError as e:
            abort(grpc_to_http_status.get(e.code(), 500), description=e.details())

        except CircuitBreakerException as e:
            abort(500, description=str(e))


@app.route('/scooters/<int:scooter_id>', methods=['GET'])
def get_scooter(scooter_id):
    while True:
        try:
            with get_scooter_service_channel("scooters") as channel:
                stub = scooters_pb2_grpc.ScooterServiceStub(channel)
                request_data = scooters_pb2.GetScooterRequest(id=scooter_id)
                response = scooters_circuit_breaker.call(lambda: stub.GetScooter(request_data, timeout=5.0))

                scooter = {
                    "id": response.id,
                    "label": response.label,
                    "battery_life": response.battery,
                    "location": response.location,
                    "is_charging": response.is_charging,
                    "available": response.available
                }
                redis_hash_ring.set(f'scooter_{scooter_id}', scooter)

                return scooter

        except RerouteException as e:
            logging.info(f"Reroute request")
            continue
        except grpc.RpcError as e:
            abort(grpc_to_http_status.get(e.code(), 500), description=e.details())
        except CircuitBreakerException as e:
            abort(500, description=str(e))

@app.route('/scooters', methods=['GET'])
def get_all_scooters():
    while True:
        try:
            with get_scooter_service_channel("scooters") as channel:
                stub = scooters_pb2_grpc.ScooterServiceStub(channel)
                response = scooters_circuit_breaker.call(
                    lambda: stub.GetAllScooters(service_discovery_pb2.Empty(), timeout=5.0))

                scooters = [scooter_to_dict(scooter) for scooter in response.scooters]
                redis_hash_ring.set('all_scooters', scooters)

                return scooters
        except RerouteException as e:
            logging.info(f"Reroute request from {channel}")
            continue
        except grpc.RpcError as e:
            abort(grpc_to_http_status.get(e.code(), 500), description=e.details())

        except CircuitBreakerException as e:
            abort(500, description=str(e))


@app.route('/scooters/<int:scooter_id>', methods=['PATCH'])
def update_scooter(scooter_id):
    while True:
        data = request.json
        request_data = scooters_pb2.UpdateScooterRequest(
            id=scooter_id,
            label=data['label'],
            battery=data['battery_life'],
            location=data['location'],
            is_charging=data['is_charging']
        )
        try:
            with get_scooter_service_channel("scooters") as channel:
                stub = scooters_pb2_grpc.ScooterServiceStub(channel)
                scooters_circuit_breaker.call(lambda: stub.UpdateScooter(request_data, timeout=5.0))

                cache_key = f'scooter_{scooter_id}'
                redis_hash_ring.delete(cache_key)
                redis_hash_ring.delete('all_scooters')
                return '', 204

        except RerouteException as e:
            continue
        except grpc.RpcError as e:
            abort(grpc_to_http_status.get(e.code(), 500), description=e.details())

        except CircuitBreakerException as e:
            abort(500, description=str(e))

@app.route('/scooters/<int:scooter_id>', methods=['DELETE'])
def delete_scooter(scooter_id):
    while True:
        try:
            with get_scooter_service_channel("scooters") as channel:
                stub = scooters_pb2_grpc.ScooterServiceStub(channel)
                scooters_circuit_breaker.call(
                    lambda: stub.DeleteScooter(scooters_pb2.DeleteScooterRequest(id=scooter_id), timeout=5.0))

                cache_key = f'scooter_{scooter_id}'
                redis_hash_ring.delete(cache_key)
                redis_hash_ring.delete('all_scooters')
            return '', 204
        except RerouteException as e:
            continue
        except grpc.RpcError as e:
            abort(grpc_to_http_status.get(e.code(), 500), description=e.details())

        except CircuitBreakerException as e:
            abort(500, description=str(e))


@app.route('/scooters', methods=['POST'])
def create_scooter():
    while True:
        data = request.json

        request_data = scooters_pb2.CreateScooterRequest(
            label=data['label'],
            battery=data['battery_life'],
            location=data['location'],
            is_charging=data['is_charging']
        )

        try:
            with get_scooter_service_channel("scooters") as channel:
                stub = scooters_pb2_grpc.ScooterServiceStub(channel)
                response = scooters_circuit_breaker.call(lambda: stub.CreateScooter(request_data, timeout=5.0))
            redis_hash_ring.delete('all_scooters')

            return scooter_to_dict(response), 201
        except RerouteException as e:
            continue
        except grpc.RpcError as e:
            abort(grpc_to_http_status.get(e.code(), 500), description=e.details())

        except CircuitBreakerException as e:
            abort(500, description=str(e))




def scooter_to_dict(object):
    return {
        "id": object.id,
        "label": object.label,
        "battery_life": object.battery,
        "location": object.location,
        "is_charging": object.is_charging,
        "available": object.available,
    }


@app.errorhandler(500)
def internal_error(error):
    return error.description, 500


@app.errorhandler(404)
def not_found_error(error):
    return error.description, 404


if __name__ == "__main__":
    app.run(debug=True, port=2050, host="api-gateway", threaded=True)
