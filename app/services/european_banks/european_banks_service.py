from google.protobuf.json_format import MessageToDict
from mongoengine.queryset import NotUniqueError
from ...protos import EuropeanBanksServicer, EuropeanBanksMultipleResponse, EuropeanBanksResponse, EuropeanBanksTableResponse, EuropeanBankEmpty, add_EuropeanBanksServicer_to_server
from ...utils import parser_all_object, parser_one_object, not_exist_code, exist_code, paginate, parser_context, pagination, default_paginate_schema
from ...utils.validate_session import is_auth
from ..bootstrap import grpc_server
from bson.objectid import ObjectId
from ...models import EuropeanBanks

class EuropeanBanksService(EuropeanBanksServicer):
    def table(self, request, context):
        auth_token = parser_context(context, 'auth_token')
        is_auth(auth_token, '04_european_banks_table')

        search = request.search

        pipeline = [
            {
                "$match": {
                    "$or": [
                        {"bankName": {"$regex": search, "$options": "i"}},
                        {"iban": {"$regex": search, "$options": "i"}},
                        {"country": {"$regex": search, "$options": "i"}},
                        {"swift": {"$regex": search, "$options": "i"}},
                    ]
                }
            },
            {
                "$set": {
                    "id": {"$toString": "$_id"}
                }
            },
            {
                "$project": {
                    "_id": 0
                }
            }
        ]

        pipeline = pipeline + pagination(request.page, request.per_page, {"bankName": 1})

        response = EuropeanBanks.objects().aggregate(pipeline)

        response = EuropeanBanksTableResponse(**default_paginate_schema(response, request.page, request.per_page))
        
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
