import grpc
import american_banks_pb2, american_banks_pb2_grpc

channel = grpc.insecure_channel('localhost:50053')
stub = american_banks_pb2_grpc.AmericanBanksStub(channel)


request = american_banks_pb2.AmericanBankNotIdRequest(
	routingNumber = '123456789',
	bankName = 'Gerard bank',
	fullName = 'Gerard Miot',
	swift = '1234567890A',
	ach = 'nothing',
	numberAccount = '12345678901234567890',
	type = 0,
	documentIdentification = '162728182',
	currency = 'dolar',
)

response = stub.save(request)


