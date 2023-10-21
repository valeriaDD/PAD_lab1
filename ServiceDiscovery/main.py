import grpc
import logging
from concurrent import futures
from proto import service_discovery_pb2 as pb2
from proto import service_discovery_pb2_grpc as pb2_grpc


logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(name)s | [%(levelname)s]: %(message)s")
service_registry = {}


class ServiceDiscovery(pb2_grpc.ServiceRegistryServicer):
    def RegisterService(self, request, context):
        logging.info(f"Received registration request for service {request.service_name} at {request.host}:{request.port}")
        service_registry[request.service_name] = (request.host, request.port)
        return pb2.Empty()

    def DiscoverService(self, request, context):
        logging.info(f"Received service discovery request for service {request.service_name}")
        if request.service_name in service_registry:
            host, port = service_registry[request.service_name]
            return pb2.ServiceInfo(service_name=request.service_name, host=host, port=port)
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Service not found")
            return pb2.Empty()

    def CheckHealth(self, request, context):
        logging.info("Received health check request")
        return pb2.HealthStatus(status=True)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    pb2_grpc.add_ServiceRegistryServicer_to_server(ServiceDiscovery(), server)
    server.add_insecure_port("[::]:2000")  # Change the port as needed
    logging.info("Service discovery server started on port 2000")
    server.start()
    server.wait_for_termination()
    logging.info("Service discovery server stopped")


if __name__ == "__main__":
    logging.info("hi!!")
    serve()
