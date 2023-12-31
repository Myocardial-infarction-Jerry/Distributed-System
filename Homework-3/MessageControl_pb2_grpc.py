# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import MessageControl_pb2 as MessageControl__pb2


class MessageControlStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Upload = channel.unary_unary(
                '/MessageControl/Upload',
                request_serializer=MessageControl__pb2.UploadRequest.SerializeToString,
                response_deserializer=MessageControl__pb2.UploadResponse.FromString,
                )
        self.Fetch = channel.unary_unary(
                '/MessageControl/Fetch',
                request_serializer=MessageControl__pb2.FetchRequest.SerializeToString,
                response_deserializer=MessageControl__pb2.FetchResponse.FromString,
                )


class MessageControlServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Upload(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Fetch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MessageControlServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Upload': grpc.unary_unary_rpc_method_handler(
                    servicer.Upload,
                    request_deserializer=MessageControl__pb2.UploadRequest.FromString,
                    response_serializer=MessageControl__pb2.UploadResponse.SerializeToString,
            ),
            'Fetch': grpc.unary_unary_rpc_method_handler(
                    servicer.Fetch,
                    request_deserializer=MessageControl__pb2.FetchRequest.FromString,
                    response_serializer=MessageControl__pb2.FetchResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'MessageControl', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MessageControl(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Upload(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MessageControl/Upload',
            MessageControl__pb2.UploadRequest.SerializeToString,
            MessageControl__pb2.UploadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Fetch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MessageControl/Fetch',
            MessageControl__pb2.FetchRequest.SerializeToString,
            MessageControl__pb2.FetchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
