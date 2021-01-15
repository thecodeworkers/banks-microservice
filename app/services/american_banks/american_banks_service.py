from google.protobuf.json_format import MessageToDict
from mongoengine.queryset import NotUniqueError
from ...protos import AmericanBanksServicer, AmericanBanksMultipleResponse, AmericanBanksResponse, AmericanBanksTableResponse, AmericanBankEmpty, add_AmericanBanksServicer_to_server
from ...utils import parser_all_object, parser_one_object, not_exist_code, exist_code, paginate, parser_context
from ...utils.validate_session import is_auth
from ..bootstrap import grpc_server
from bson.objectid import ObjectId
from ...models import AmericanBanks

class AmericanBanksService(AmericanBanksServicer):
    def table(self, request, context):
        
        auth_token = parser_context(context, 'auth_token')
        is_auth(auth_token, '04_american_banks_table')

        us_banks = AmericanBanks.objects

        if request.search:
            us_banks = AmericanBanks.objects(__raw__={'$or': [
                {'bankName': request.search},
                {'routingNumber':  request.search},
                {'swift': request.search},
                {'_id': ObjectId(request.search) if ObjectId.is_valid(
                    request.search) else request.search}
            ]})
            
        response = paginate(us_banks, request.page)
        response = AmericanBanksTableResponse(**response)
        
        return response

    def get_all(self, request, context):
        auth_token = parser_context(context, 'auth_token')
        is_auth(auth_token, '04_american_banks_get_all')
        
        us_banks = parser_all_object(AmericanBanks.objects.all())
        response = AmericanBanksMultipleResponse(american=us_banks)

        return response

    def get(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')

            is_auth(auth_token, '04_american_banks_get')
            us_banks = AmericanBanks.objects.get(id=request.id)
            us_banks = parser_one_object(us_banks)
            response = AmericanBanksResponse(american=us_banks)

            return response

        except AmericanBanks.DoesNotExist as e:
            not_exist_code(context, e)

    def save(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '04_american_banks_save')
            
            american_banks_object = MessageToDict(request)
            us_banks = AmericanBanks(**american_banks_object).save()
            us_banks = parser_one_object(us_banks)
            response = AmericanBanksResponse(american=us_banks)

            return response

        except NotUniqueError as e:
            exist_code(context, e)

    def update(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '04_american_banks_update')
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
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '04_american_banks_delete')
            us_banks = AmericanBanks.objects.get(id=request.id)
            us_banks = us_banks.delete()
            response = AmericanBankEmpty()

            return response

        except AmericanBanks.DoesNotExist as e:
            not_exist_code(context, e)

def start_americanbanks_service():
    add_AmericanBanksServicer_to_server(AmericanBanksService(), grpc_server)
