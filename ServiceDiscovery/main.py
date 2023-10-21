import threading
import time

import grpc
import logging
from concurrent import futures
from proto import service_discovery_pb2 as pb2
from proto import service_discovery_pb2_grpc as pb2_grpc
import itertools

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(name)s | [%(levelname)s]: %(message)s")


class ServiceDiscovery(pb2_grpc.ServiceRegistryServicer):
    def __init__(self):
        self.service_instances = {}
        self.round_robin = {}

        health_check_thread = threading.Thread(target=self.periodic_health_check)
        health_check_thread.daemon = True
        health_check_thread.start()

    def RegisterService(self, request, context):
        logging.info(f"Registration  for service {request.service_name} at {request.host}:{request.port}")

        if request.service_name not in self.service_instances:
            self.service_instances[request.service_name] = []

        self.service_instances[request.service_name].append((request.host, request.port))
        self.round_robin[request.service_name] = itertools.cycle(self.service_instances[request.service_name])

        return pb2.Empty()

    def DiscoverService(self, request, context):
        logging.info(f"Received service discovery request for service {request.service_name}")

        if request.service_name in self.round_robin:
            host, port = next(self.round_robin[request.service_name])
            return pb2.ServiceInfo(service_name=request.service_name, host=host, port=port)

        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details("Service not found")
        return pb2.Empty()

    def CheckHealth(self, request, context):
        logging.info("Received health check request")
        return pb2.HealthStatus(status=True)

    def periodic_health_check(self):
        while True:
            for service_name, instances in self.service_instances.items():
                instances_to_remove = []

                for host, port in instances:
                    is_healthy = self.check_service_health(host, port)
                    if not is_healthy:
                        instances_to_remove.append((host, port))

                for host, port in instances_to_remove:
                    instances.remove((host, port))
                    logging.info(f"Removed service {service_name} at {host}:{port} from the list of available services")

                self.round_robin[service_name] = itertools.cycle(instances)

            time.sleep(30)

    def check_service_health(self, host, port):
        try:
            channel = grpc.insecure_channel(f"{host}:{port}")
            stub = pb2_grpc.ServiceRegistryStub(channel)
            response = stub.CheckHealth(pb2.Empty())
            is_healthy = response.status
            channel.close()

            return is_healthy
        except Exception as e:
            return False


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    pb2_grpc.add_ServiceRegistryServicer_to_server(ServiceDiscovery(), server)
    server.add_insecure_port("[::]:2000")  # Change the port as needed
    logging.info("Service discovery server started on port 2000")
    server.start()
    server.wait_for_termination()
    logging.info("Service discovery server stopped")


if __name__ == "__main__":
    serve()
