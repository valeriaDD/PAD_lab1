# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from proto import scooters_pb2 as proto_dot_scooters__pb2
from proto import service_discovery_pb2 as proto_dot_service__discovery__pb2


class ScooterServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetScooter = channel.unary_unary(
                '/ScooterService/GetScooter',
                request_serializer=proto_dot_scooters__pb2.GetScooterRequest.SerializeToString,
                response_deserializer=proto_dot_scooters__pb2.GetScooterResponse.FromString,
                )
        self.GetAllScooters = channel.unary_unary(
                '/ScooterService/GetAllScooters',
                request_serializer=proto_dot_service__discovery__pb2.Empty.SerializeToString,
                response_deserializer=proto_dot_scooters__pb2.GetAllScootersResponse.FromString,
                )
        self.UpdateScooter = channel.unary_unary(
                '/ScooterService/UpdateScooter',
                request_serializer=proto_dot_scooters__pb2.UpdateScooterRequest.SerializeToString,
                response_deserializer=proto_dot_service__discovery__pb2.Empty.FromString,
                )
        self.DeleteScooter = channel.unary_unary(
                '/ScooterService/DeleteScooter',
                request_serializer=proto_dot_scooters__pb2.DeleteScooterRequest.SerializeToString,
                response_deserializer=proto_dot_service__discovery__pb2.Empty.FromString,
                )
        self.CreateScooter = channel.unary_unary(
                '/ScooterService/CreateScooter',
                request_serializer=proto_dot_scooters__pb2.CreateScooterRequest.SerializeToString,
                response_deserializer=proto_dot_scooters__pb2.CreateScooterResponse.FromString,
                )


class ScooterServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetScooter(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllScooters(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateScooter(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteScooter(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateScooter(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ScooterServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetScooter': grpc.unary_unary_rpc_method_handler(
                    servicer.GetScooter,
                    request_deserializer=proto_dot_scooters__pb2.GetScooterRequest.FromString,
                    response_serializer=proto_dot_scooters__pb2.GetScooterResponse.SerializeToString,
            ),
            'GetAllScooters': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllScooters,
                    request_deserializer=proto_dot_service__discovery__pb2.Empty.FromString,
                    response_serializer=proto_dot_scooters__pb2.GetAllScootersResponse.SerializeToString,
            ),
            'UpdateScooter': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateScooter,
                    request_deserializer=proto_dot_scooters__pb2.UpdateScooterRequest.FromString,
                    response_serializer=proto_dot_service__discovery__pb2.Empty.SerializeToString,
            ),
            'DeleteScooter': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteScooter,
                    request_deserializer=proto_dot_scooters__pb2.DeleteScooterRequest.FromString,
                    response_serializer=proto_dot_service__discovery__pb2.Empty.SerializeToString,
            ),
            'CreateScooter': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateScooter,
                    request_deserializer=proto_dot_scooters__pb2.CreateScooterRequest.FromString,
                    response_serializer=proto_dot_scooters__pb2.CreateScooterResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ScooterService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ScooterService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetScooter(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ScooterService/GetScooter',
                                             proto_dot_scooters__pb2.GetScooterRequest.SerializeToString,
                                             proto_dot_scooters__pb2.GetScooterResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllScooters(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ScooterService/GetAllScooters',
                                             proto_dot_service__discovery__pb2.Empty.SerializeToString,
                                             proto_dot_scooters__pb2.GetAllScootersResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateScooter(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ScooterService/UpdateScooter',
                                             proto_dot_scooters__pb2.UpdateScooterRequest.SerializeToString,
                                             proto_dot_service__discovery__pb2.Empty.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteScooter(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ScooterService/DeleteScooter',
                                             proto_dot_scooters__pb2.DeleteScooterRequest.SerializeToString,
                                             proto_dot_service__discovery__pb2.Empty.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateScooter(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ScooterService/CreateScooter',
                                             proto_dot_scooters__pb2.CreateScooterRequest.SerializeToString,
                                             proto_dot_scooters__pb2.CreateScooterResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)