import grpc
import american_banks_pb2, american_banks_pb2_grpc

channel = grpc.insecure_channel('localhost:50053')
stub = american_banks_pb2_grpc.AmericanBanksStub(channel)


request = american_banks_pb2.AmericanBankRequest(
	id = '1234567',
	routingNumber = '123456789',
	bankName = 'Gerard bank',
	swift = '1234567890A',
	fullName = 'Gerard Miot',
	numberAccount = '11111111111111111111',
	# address_user = 'El Cafetal',
	type = "current",
	# user_address = 'Agua Salud',
	# document_identification = '12345678',
	currency = 'dolar'
)

response = stub.save(request)
print(response)



