from google.protobuf.json_format import MessageToDict
from mongoengine.queryset import NotUniqueError
from ...protos import AmericanBanksServicer, AmericanBanksMultipleResponse, AmericanBanksResponse, AmericanBanksTableResponse, add_AmericanBanksServicer_to_server
from ...utils import parser_all_object, parser_one_object, not_exist_code, exist_code, paginate
from ..bootstrap import grpc_server
from ...models import AmericanBanks

class AmericanBanksService(AmericanBanksServicer):
    def table(self, request, context):
        us_banks = AmericanBanks.objects
        us_banks = paginate(us_banks, request.page)
        response = AmericanBanksTableResponse(**response)
        
        return response

    def get_all(self, request, context):
        us_banks = parser_all_object(AmericanBanks.objects.all())
        response = AmericanBanksMultipleResponse(american=us_banks)

        return response

    def get(self, request, context):
        try:
            us_banks = AmericanBanks.objects.get(id=request.id)
            us_banks = parser_one_object(us_banks)
            response = AmericanBanksResponse(american=us_banks)

            return response

        except AmericanBanks.DoesNotExist as e:
            not_exist_code(context, e)

    def save(self, request, context):
        try:
            american_banks_object = MessageToDict(request)
            us_banks = AmericanBanks(**american_banks_object).save()
            us_banks = parser_one_object(us_banks)
            response = AmericanBanksResponse(american=us_banks)

            return response

        except NotUniqueError as e:
            exist_code(context, e)

    def update(self, request, context):
        try:
            american_banks_object = MessageToDict(request)
            us_banks = AmericanBanks.objects(id=american_banks_object['id'])

            if not us_banks: del american_banks_object['id']

            us_banks = AmericanBanks(**american_banks_object).save()
            us_banks = parser_one_object(us_banks)
            response = AmericanBanksResponse(american=us_banks)
        
            return response

        except NotUniqueError as e:
            exist_code(context, e)
        
    def delete(self, request, context):
        try:
            us_banks = AmericanBanks.objects.get(id=request.id)
            us_banks = us_banks.delete()
            us_banks = AmericanBanksEmpty()

            return response

        except AmericanBanks.DoesNotExist as e:
            not_exist_code(context, e)

def start_americanbanks_service():
    add_AmericanBanksServicer_to_server(AmericanBanksService(), grpc_server)
