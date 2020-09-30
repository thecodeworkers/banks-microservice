from google.protobuf.json_format import MessageToDict
from mongoengine.queryset import NotUniqueError
from ...protos import EuropeanBanksServicer, EuropeanBanksMultipleResponse, EuropeanBanksResponse, EuropeanBanksTableResponse, EuropeanBankEmpty, add_EuropeanBanksServicer_to_server
from ...utils import parser_all_object, parser_one_object, not_exist_code, exist_code, paginate
from ...utils.validate_session import is_auth
from ..bootstrap import grpc_server
from ...models import EuropeanBanks

class EuropeanBanksService(EuropeanBanksServicer):
    def table(self, request, context):
        metadata = dict(context.invocation_metadata())
        is_auth(metadata['auth_token'], '04_european_banks_table')
        eu_banks = EuropeanBanks.objects
        eu_banks = paginate(eu_banks, request.page)
        response = EuropeanBanksTableResponse(**response)
        
        return response

    def get_all(self, request, context):
        metadata = dict(context.invocation_metadata())
        is_auth(metadata['auth_token'], '04_european_banks_get_all')
        eu_banks = parser_all_object(EuropeanBanks.objects.all())
        response = EuropeanBanksMultipleResponse(european=eu_banks)

        return response

    def get(self, request, context):
        try:
            metadata = dict(context.invocation_metadata())
            is_auth(metadata['auth_token'], '04_european_banks_get')
            eu_banks = EuropeanBanks.objects.get(id=request.id)
            eu_banks = parser_one_object(eu_banks)
            response = EuropeanBanksResponse(european=eu_banks)

            return response

        except EuropeanBanks.DoesNotExist as e:
            not_exist_code(context, e)

    def save(self, request, context):
        try:
            metadata = dict(context.invocation_metadata())
            is_auth(metadata['auth_token'], '04_european_banks_save')
            european_banks_object = MessageToDict(request)
            eu_banks = EuropeanBanks(**european_banks_object).save()
            eu_banks = parser_one_object(eu_banks)
            response = EuropeanBanksResponse(european=eu_banks)

            return response

        except NotUniqueError as e:
            exist_code(context, e)

    def update(self, request, context):
        try:
            metadata = dict(context.invocation_metadata())
            is_auth(metadata['auth_token'], '04_european_banks_update')
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
            metadata = dict(context.invocation_metadata())
            is_auth(metadata['auth_token'], '04_european_banks_delete')
            eu_banks = EuropeanBanks.objects.get(id=request.id)
            eu_banks = eu_banks.delete()
            response = EuropeanBankEmpty()

            return response

        except EuropeanBanks.DoesNotExist as e:
            not_exist_code(context, e)

def start_europeanbanks_service():
    add_EuropeanBanksServicer_to_server(EuropeanBanksService(), grpc_server)
