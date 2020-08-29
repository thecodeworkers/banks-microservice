import grpc
import credit_cards_pb2, credit_cards_pb2_grpc

channel = grpc.insecure_channel('localhost:50053')
stub = credit_cards_pb2_grpc.CreditCardsStub(channel)


request = credit_cards_pb2.CreditCardNotIdRequest(
    cardNumber = '123456789012345',
    username = 'Giberson Lara',
    cvc = '123',
    expiration = '03/2020', 
    documentIdentification = '123456789'
)

print(request)
response = stub.save(request)

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