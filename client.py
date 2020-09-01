import grpc
import latinamerican_banks_pb2, latinamerican_banks_pb2_grpc

channel = grpc.insecure_channel('localhost:50053')
stub = latinamerican_banks_pb2_grpc.LatinAmericanBanksStub(channel)


request = latinamerican_banks_pb2.LatinAmericanBankIdRequest(
    # cardNumber = '123456789012345',
    # username = 'Kevin',
    # cvc = '123',
    # expiration = '03/2020', 
    # documentIdentification = '123456789'
    id = '5f4dd46f805377a7c3620330',
    # bankName = 'Banco Mercantil',
    # swift = 'ASDERGHUXXX',
    # country = 'Venezuela'
    # # fullName = 'Giber',
    # swift = 'ABCDEFDHIJ',
    # country = 'España',
    # iban = ''
    # iban = '123'
    # iban = '1234',
    # currency = 'euro',
    # numberAccount = '123456789086432345',
    # bankAddress = 'Barcelona, España',
    # userAddress = 'Barcelona, España',
    # type = 0,
    # documentIdentification = '1234567890'
    # id = '5f4c3c4540f621b9a7478d27'
)

print(request)
response = stub.delete(request)

print(response)

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

# request_data= {
#   'id': '5f458a1f41ba1b31f53af306'
# }

# response = stub.save(request)


# request = american_banks_pb2.AmericanBankIdRequest(id="5f457c547ee9792a16027368")
# request = american_banks_pb2.AmericanBankEmpty()
# request = american_banks_pb2.AmericanBankRequest(**request_data)
# request = american_banks_pb2.AmericanBankIdRequest(**request_data)


# response = stub.delete(request)

# print(response)