from google.protobuf.json_format import MessageToDict
from mongoengine.queryset import NotUniqueError
from ...protos import CreditCardsServicer, CreditCardsMultipleResponse, CreditCardsResponse, CreditCardsTableResponse, CreditCardEmpty, add_CreditCardsServicer_to_server
from ...utils import parser_all_object, parser_one_object, not_exist_code, exist_code, paginate
from ..bootstrap import grpc_server
from ...models import CreditCards

class CreditCardsService(CreditCardsServicer):
    def table(self, request, context):
        card_credit = CreditCards.objects
        card_credit = paginate(card_credit, request.page)
        response = CreditCardsTableResponse(**response)
        
        return response

    def get_all(self, request, context):
        card_credit = parser_all_object(CreditCards.objects.all())
        response = CreditCardsMultipleResponse(credit=card_credit)

        return response

    def get(self, request, context):
        try:
            card_credit = CreditCards.objects.get(id=request.id)
            card_credit = parser_one_object(card_credit)
            response = CreditCardsResponse(credit=card_credit)

            return response

        except AmericanBanks.DoesNotExist as e:
            not_exist_code(context, e)

    def save(self, request, context):
        try:
            credit_cards_object = MessageToDict(request)
            card_credit = CreditCards(**credit_cards_object).save()
            card_credit = parser_one_object(card_credit)
            response = CreditCardsResponse(credit=card_credit)

            return response

        except NotUniqueError as e:
            exist_code(context, e)

    def update(self, request, context):
        try:
            credit_cards_object = MessageToDict(request)
            card_credit = CreditCards.objects(id=credit_cards_object['id'])

            if not card_credit: del credit_cards_object['id']

            card_credit = CreditCards(**credit_cards_object).save()
            card_credit = parser_one_object(card_credit)
            response = CreditCardsResponse(credit=card_credit)
        
            return response

        except NotUniqueError as e:
            exist_code(context, e)
        
    def delete(self, request, context):
        try:
            card_credit = AmericanBanks.objects.get(id=request.id)
            us_banks = us_banks.delete()
            response = AmericanBankEmpty()

            return response

        except AmericanBanks.DoesNotExist as e:
            not_exist_code(context, e)

def start_creditcards_service():
    add_CreditCardsServicer_to_server(CreditCardsService(), grpc_server)
