from google.protobuf.json_format import MessageToDict
from mongoengine.queryset import NotUniqueError
from ...protos import LatinAmericanBanksServicer, LatinAmericanBanksMultipleResponse, LatinAmericanBanksResponse, LatinAmericanBanksTableResponse, LatinAmericanBankEmpty, add_LatinAmericanBanksServicer_to_server
from ...utils import parser_all_object, parser_one_object, not_exist_code, exist_code, paginate, parser_context
from ...utils.validate_session import is_auth
from ..bootstrap import grpc_server
from ...models import LatinAmericanBanks

class LatinAmericanBanksService(LatinAmericanBanksServicer):
    def table(self, request, context):
        auth_token = parser_context(context, 'auth_token')
        is_auth(auth_token, '04_latin_american_banks_table')
        latin_banks = LatinAmericanBanks.objects
        latin_banks = paginate(latin_banks, request.page)
        response = LatinAmericanBanksTableResponse(**response)
        
        return response

    def get_all(self, request, context):
        auth_token = parser_context(context, 'auth_token')
        is_auth(auth_token, '04_latin_american_banks_get_all')
        latin_banks = parser_all_object(LatinAmericanBanks.objects.all())
        response = LatinAmericanBanksMultipleResponse(latin=latin_banks)

        return response

    def get(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '04_latin_american_banks_get')
            latin_banks = LatinAmericanBanks.objects.get(id=request.id)
            latin_banks = parser_one_object(latin_banks)
            response = LatinAmericanBanksResponse(latin=latin_banks)

            return response

        except LatinAmericanBanks.DoesNotExist as e:
            not_exist_code(context, e)

    def save(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '04_latin_american_banks_save')
            latinamerican_banks_object = MessageToDict(request)
            latin_banks = LatinAmericanBanks(**latinamerican_banks_object).save()
            latin_banks = parser_one_object(latin_banks)
            response = LatinAmericanBanksResponse(latin=latin_banks)

            return response

        except NotUniqueError as e:
            exist_code(context, e)

    def update(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '04_latin_american_banks_update')
            latinamerican_banks_object = MessageToDict(request)
            latin_banks = LatinAmericanBanks.objects(id=latinamerican_banks_object['id'])

            if not latin_banks: del latinamerican_banks_object['id']

            latin_banks = LatinAmericanBanks(**latinamerican_banks_object).save()
            latin_banks = parser_one_object(latin_banks)
            response = LatinAmericanBanksResponse(latin=latin_banks)
        
            return response

        except NotUniqueError as e:
            exist_code(context, e)
        
    def delete(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '04_latin_american_banks_delete')
            latin_banks = LatinAmericanBanks.objects.get(id=request.id)
            latin_banks = latin_banks.delete()
            response = LatinAmericanBankEmpty()

            return response

        except LatinAmericanBanks.DoesNotExist as e:
            not_exist_code(context, e)

def start_latinamericanbanks_service():
    add_LatinAmericanBanksServicer_to_server(LatinAmericanBanksService(), grpc_server)
