# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import cityinformation_pb2 as cityinformation__pb2


class CityServiceStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCityInformation = channel.unary_unary(
                '/cityinformation.CityService/GetCityInformation',
                request_serializer=cityinformation__pb2.SearchRequest.SerializeToString,
                response_deserializer=cityinformation__pb2.SearchResponse.FromString,
                )


class CityServiceServicer(object):
    """Missing associated documentation comment in .proto file"""

    def GetCityInformation(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CityServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetCityInformation': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCityInformation,
                    request_deserializer=cityinformation__pb2.SearchRequest.FromString,
                    response_serializer=cityinformation__pb2.SearchResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cityinformation.CityService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CityService(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def GetCityInformation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cityinformation.CityService/GetCityInformation',
            cityinformation__pb2.SearchRequest.SerializeToString,
            cityinformation__pb2.SearchResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
