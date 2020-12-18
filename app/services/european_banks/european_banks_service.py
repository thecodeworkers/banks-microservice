from google.protobuf.json_format import MessageToDict
from mongoengine.queryset import NotUniqueError
from ...protos import EuropeanBanksServicer, EuropeanBanksMultipleResponse, EuropeanBanksResponse, EuropeanBanksTableResponse, EuropeanBankEmpty, add_EuropeanBanksServicer_to_server
from ...utils import parser_all_object, parser_one_object, not_exist_code, exist_code, paginate, parser_context
from ...utils.validate_session import is_auth
from ..bootstrap import grpc_server
from bson.objectid import ObjectId
from ...models import EuropeanBanks

class EuropeanBanksService(EuropeanBanksServicer):
    def table(self, request, context):
        auth_token = parser_context(context, 'auth_token')
        is_auth(auth_token, '04_european_banks_table')
        eu_banks = EuropeanBanks.objects

        if request.search:
            eu_banks = EuropeanBanks.objects(__raw__={'$or': [
                {'bankName': request.search},
                {'iban':  request.search},
                {'country':  request.search},
                {'swift': request.search},
                {'_id': ObjectId(request.search) if ObjectId.is_valid(
                    request.search) else request.search}
            ]})

        response = paginate(eu_banks, request.page)
        response = EuropeanBanksTableResponse(**response)
        
        return response

    def get_all(self, request, context):
        auth_token = parser_context(context, 'auth_token')
        is_auth(auth_token, '04_european_banks_get_all')
        eu_banks = parser_all_object(EuropeanBanks.objects.all())
        response = EuropeanBanksMultipleResponse(european=eu_banks)

        return response

    def get(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '04_european_banks_get')
            eu_banks = EuropeanBanks.objects.get(id=request.id)
            eu_banks = parser_one_object(eu_banks)
            response = EuropeanBanksResponse(european=eu_banks)

            return response

        except EuropeanBanks.DoesNotExist as e:
            not_exist_code(context, e)

    def save(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '04_european_banks_save')
            european_banks_object = MessageToDict(request)
            eu_banks = EuropeanBanks(**european_banks_object).save()
            eu_banks = parser_one_object(eu_banks)
            response = EuropeanBanksResponse(european=eu_banks)

            return response

        except NotUniqueError as e:
            exist_code(context, e)

    def update(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '04_european_banks_update')
            european_banks_object = MessageToDict(request)
            eu_banks = EuropeanBanks.objects(id=european_banks_object['id'])

            if not eu_banks: del european_banks_object['id']

            eu_banks = EuropeanBanks(**european_banks_object).save()
            eu_banks = parser_one_object(eu_banks)
            response = EuropeanBanksResponse(european=eu_banks)
        
            return response

        except NotUniqueError as e:
            exist_code(context, e)
        
    def delete(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '04_european_banks_delete')
            eu_banks = EuropeanBanks.objects.get(id=request.id)
            eu_banks = eu_banks.delete()
            response = EuropeanBankEmpty()

            return response

        except EuropeanBanks.DoesNotExist as e:
            not_exist_code(context, e)

def start_europeanbanks_service():
    add_EuropeanBanksServicer_to_server(EuropeanBanksService(), grpc_server)
