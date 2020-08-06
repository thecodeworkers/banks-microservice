from ...protos import test_pb2, test_pb2_grpc
from ..bootstrap import grpc_server

class TestService(test_pb2_grpc.TestServiceServicer):
  def SaveTesting(self, request, context):
    print('jeje')
    name = request.name
    response = test_pb2.saveTestResponse(name={
      'name': 'Giber'
    })
    return response

def start_test_service():
  test_pb2_grpc.add_TestServiceServicer_to_server(TestService(), grpc_server)
