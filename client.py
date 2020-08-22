import grpc
import american_banks_pb2, american_banks_pb2_grpc

channel = grpc.insecure_channel('localhost:50055')
stub = american_banks_pb2_grpc.AmericanBanksStub(channel)


# request = american_banks_pb2.AmericanBankNotIdRequest(
# 	routingNumber = '123456789',
# 	bankName = 'Gerard bank',
# 	fullName = 'Gerard Miot',
# 	swift = '1234567890A',
# 	ach = 'nothing',
# 	numberAccount = '12345678901234567890',
# 	type = 0,
# 	documentIdentification = '162728182',
# 	currency = 'dolar',
# )

# response = stub.save(request)


request = american_banks_pb2.AmericanBankIdRequest(id="5f40a2ac92a5b18c591de192")
response = stub.get(request);

print(response)
