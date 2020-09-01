from google.protobuf.json_format import MessageToDict
from mongoengine.queryset import NotUniqueError
from ...protos import LatinAmericanBanksServicer, LatinAmericanBanksMultipleResponse, LatinAmericanBanksResponse, LatinAmericanBanksTableResponse, LatinAmericanBankEmpty, add_LatinAmericanBanksServicer_to_server
from ...utils import parser_all_object, parser_one_object, not_exist_code, exist_code, paginate
from ..bootstrap import grpc_server
from ...models import LatinAmericanBanks

class LatinAmericanBanksService(LatinAmericanBanksServicer):
    def table(self, request, context):
        latin_banks = LatinAmericanBanks.objects
        latin_banks = paginate(latin_banks, request.page)
        response = LatinAmericanBanksTableResponse(**response)
        
        return response

    def get_all(self, request, context):
        latin_banks = parser_all_object(LatinAmericanBanks.objects.all())
        response = LatinAmericanBanksMultipleResponse(latin=latin_banks)

        return response

    def get(self, request, context):
        try:
            latin_banks = LatinAmericanBanks.objects.get(id=request.id)
            latin_banks = parser_one_object(latin_banks)
            response = LatinAmericanBanksResponse(latin=latin_banks)

            return response

        except LatinAmericanBanks.DoesNotExist as e:
            not_exist_code(context, e)

    def save(self, request, context):
        try:
            latinamerican_banks_object = MessageToDict(request)
            latin_banks = LatinAmericanBanks(**latinamerican_banks_object).save()
            latin_banks = parser_one_object(latin_banks)
            response = LatinAmericanBanksResponse(latin=latin_banks)

            return response

        except NotUniqueError as e:
            exist_code(context, e)

    def update(self, request, context):
        try:
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
            latin_banks = LatinAmericanBanks.objects.get(id=request.id)
            latin_banks = latin_banks.delete()
            response = LatinAmericanBankEmpty()

            return response

        except LatinAmericanBanks.DoesNotExist as e:
            not_exist_code(context, e)

def start_latinamericanbanks_service():
    add_LatinAmericanBanksServicer_to_server(LatinAmericanBanksService(), grpc_server)
