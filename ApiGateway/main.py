import logging

import grpc
from flask import Flask, request, abort
from flask_caching import Cache

from proto import service_discovery_pb2_grpc, service_discovery_pb2, scooters_pb2, scooters_pb2_grpc, bookings_pb2_grpc, \
    bookings_pb2

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(name)s | [%(levelname)s]: %(message)s")

config = {
    "DEBUG": True,
    "CACHE_TYPE": "redis",
    "CACHE_REDIS_URL": "redis://redis:6379/0",
    "CACHE_DEFAULT_TIMEOUT": 300
}

SERVICE_DISCOVERY_PORT = 2000
SERVICE_NAME = "service-discovery"

app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)


def get_scooter_service_channel(service_name):
    try:
        with grpc.insecure_channel(f'{SERVICE_NAME}:{SERVICE_DISCOVERY_PORT}') as channel:
            stub = service_discovery_pb2_grpc.ServiceRegistryStub(channel)
            response = stub.DiscoverService(service_discovery_pb2.ServiceRequest(service_name=service_name))
            return grpc.insecure_channel(f"{response.host}:{response.port}")
    except grpc.RpcError as e:
        abort(500, description="Service discovery failed")


@app.route("/")
@cache.cached(timeout=5)
def hello_world():
    return "hello!!"


@app.route('/book/scooters/<int:scooter_id>', methods=['POST'])
def book_scooter(scooter_id):
    data = request.json
    request_data = bookings_pb2.BookScooterRequest(
        scooter_id=str(scooter_id),
        start=data['start'],
        user_email=data['user_email'],
        title=data['title']
    )
    try:
        with get_scooter_service_channel("bookings") as channel:
            stub = bookings_pb2_grpc.BookingsServiceStub(channel)
            response = stub.BookScooter(request_data)

            cache.delete('all_bookings')
            return {
                'id': response.id,
                'title': response.title,
                'start': response.start,
                'user_email': response.user_email,
                'scooter_id': response.scooter_id,
                'end': response.end
            }

    except grpc.RpcError as e:
        abort(500, description=e.details())


@app.route('/book/<int:booking_id>/end-ride', methods=['PATCH'])
def end_ride(booking_id):
    request_data = bookings_pb2.EndRideRequest(id=booking_id)
    try:
        with get_scooter_service_channel("bookings") as channel:
            stub = bookings_pb2_grpc.BookingsServiceStub(channel)
            response = stub.EndRide(request_data)

            cache_key = f'booking_{booking_id}'
            cache.delete(cache_key)
            cache.delete('all_bookings')
            return {
                'id': response.id,
                'title': response.title,
                'start': response.start,
                'user_email': response.user_email,
                'scooter_id': response.scooter_id,
                'end': response.end
            }
    except grpc.RpcError as e:
        abort(500, description=e.details())


@app.route('/book/<int:booking_id>', methods=['GET'])
def get_booking(booking_id):
    request_data = bookings_pb2.GetBookingRequest(id=booking_id)
    try:
        with get_scooter_service_channel("bookings") as channel:
            stub = bookings_pb2_grpc.BookingsServiceStub(channel)
            response = stub.GetBooking(request_data)
            booking = {
                'id': response.id,
                'title': response.title,
                'start': response.start,
                'user_email': response.user_email,
                'scooter_id': response.scooter_id,
                'end': response.end
            }
            cache.set(f'booking_{booking_id}', booking, timeout=5)
            return booking
    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.NOT_FOUND:
            abort(404, description="Booking not found")
        abort(500, description=e.details())


@app.route('/book', methods=['GET'])
@cache.cached(timeout=5, key_prefix='all_bookings')
def get_all_bookings():
    try:
        with get_scooter_service_channel("bookings") as channel:
            stub = bookings_pb2_grpc.BookingsServiceStub(channel)
            response = stub.GetAllBookings(service_discovery_pb2.Empty())
            return [
                {
                    'id': booking.id,
                    'title': booking.title,
                    'start': booking.start,
                    'user_email': booking.user_email,
                    'scooter_id': booking.scooter_id,
                    'end': booking.end
                } for booking in response.bookings
            ]
    except grpc.RpcError as e:
        abort(500, description=e.details())


@app.route('/scooters/<int:scooter_id>', methods=['GET'])
def get_scooter(scooter_id):
    try:
        with get_scooter_service_channel("scooters") as channel:
            stub = scooters_pb2_grpc.ScooterServiceStub(channel)
            request_data = scooters_pb2.GetScooterRequest(id=scooter_id)
            response = stub.GetScooter(request_data)
            scooter = {
                "id": response.id,
                "label": response.label,
                "battery_life": response.battery,
                "location": response.location,
                "is_charging": response.is_charging
            }
            cache.set(f'scooter_{scooter_id}', scooter, timeout=5)

            return scooter

    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.NOT_FOUND:
            abort(404, description="Scooter not found")
        abort(500, description=e.details())


@app.route('/scooters', methods=['GET'])
@cache.cached(timeout=5, key_prefix='all_scooters')
def get_all_scooters():
    try:
        with get_scooter_service_channel("scooters") as channel:
            stub = scooters_pb2_grpc.ScooterServiceStub(channel)
            response = stub.GetAllScooters(service_discovery_pb2.Empty())
            logging.info(response)
            return [scooter_to_dict(scooter) for scooter in response.scooters]
    except grpc.RpcError as e:
        abort(500, description=e.details())


@app.route('/scooters/<int:scooter_id>', methods=['PATCH'])
def update_scooter(scooter_id):
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
            stub.UpdateScooter(request_data)

            cache_key = f'scooter_{scooter_id}'
            cache.delete(cache_key)
            cache.delete('all_scooters')
            return '', 204
    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.NOT_FOUND:
            abort(404, description="Scooter not found")
        abort(500, description=e.details())


@app.route('/scooters/<int:scooter_id>', methods=['DELETE'])
def delete_scooter(scooter_id):
    try:
        with get_scooter_service_channel("scooters") as channel:
            stub = scooters_pb2_grpc.ScooterServiceStub(channel)
            stub.DeleteScooter(scooters_pb2.DeleteScooterRequest(id=scooter_id))

            cache_key = f'scooter_{scooter_id}'
            cache.delete(cache_key)
            cache.delete('all_scooters')
        return '', 204
    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.NOT_FOUND:
            abort(404, description="Scooter not found")
        abort(500, description=e.details())


@app.route('/scooters', methods=['POST'])
def create_scooter():
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
            response = stub.CreateScooter(request_data)
    except grpc.RpcError as e:
        abort(500, description=e)

    cache.delete('all_scooters')
    return scooter_to_dict(response), 201

def scooter_to_dict(object):
    return {
        "id": object.id,
        "label": object.label,
        "battery_life": object.battery,
        "location": object.location,
        "is_charging": object.is_charging
    }


@app.errorhandler(500)
def internal_error(error):
    return error.description, 500


@app.errorhandler(404)
def not_found_error(error):
    return error.description, 404


if __name__ == "__main__":
    app.run(debug=True, port=2050, host="api-gateway")
