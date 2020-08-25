import grpc
import american_banks_pb2, american_banks_pb2_grpc

channel = grpc.insecure_channel('localhost:50056')
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

# request_data = {
#   'id':'5f457c547ee9792a16027368',
#   'routingNumber': '987654321',
#   'bankName': 'Gerard bank',
#   'fullName':'Gerard Miot',
#   'swift':'1234567890A',
#   'ach': 'nothing',
#   'numberAccount': '12345678901234567890',
#   'type': 0,
#   'documentIdentification':'162728182',
#   'currency':'dolar',
# }

request_data= {
  'id': '5f458a1f41ba1b31f53af306'
}

# response = stub.save(request)


# request = american_banks_pb2.AmericanBankIdRequest(id="5f457c547ee9792a16027368")
# request = american_banks_pb2.AmericanBankEmpty()
# request = american_banks_pb2.AmericanBankRequest(**request_data)
request = american_banks_pb2.AmericanBankIdRequest(**request_data)


response = stub.delete(request)

print(response)
