import grpc
import test_pb2, test_pb2_grpc

channel = grpc.insecure_channel('localhost:50053')
stub = test_pb2_grpc.TestServiceStub(channel)

request = test_pb2.Test(name = 'Giber')
response = stub.SaveTesting(request)

print(response)