from google.protobuf.json_format import MessageToDict
from mongoengine.queryset import NotUniqueError
from ...protos import CreditCardsServicer, CreditCardsMultipleResponse, CreditCardsResponse, CreditCardsTableResponse, CreditCardEmpty, add_CreditCardsServicer_to_server
from ...utils import parser_all_object, parser_one_object, not_exist_code, exist_code, paginate, parser_context, pagination, default_paginate_schema
from ...utils.validate_session import is_auth
from ..bootstrap import grpc_server
from bson.objectid import ObjectId
from ...models import CreditCards

class CreditCardsService(CreditCardsServicer):
    def table(self, request, context):

        auth_token = parser_context(context, 'auth_token')
        is_auth(auth_token, '04_credit_cards_table')

        search = request.search

        pipeline = [
            {
                "$match": {
                    "$or": [
                        {"entity": {"$regex": search, "$options": "i"}},
                        {"cvcValidation": {"$regex": search, "$options": "i"}},
                        {"numberValidation": {"$regex": search, "$options": "i"}},
                        {"regex": {"$regex": search, "$options": "i"}},
                    ]
                }
            },
            {
                "$group": {
                    "_id": "$_id",
                    "id": {"$first": {"$toString": "$_id"}},
                    "entity": {"$first": "$entity"},
                    "cvcValidation": {"$first": "$cvcValidation"},
                    "numberValidation": {"$first": "$numberValidation"},
                    "regex": {"$first": "$regex"},
                }
            },
            {
                "$project": {
                    "_id": 0
                }
            }
        ]

        pipeline = pipeline + pagination(request.page, request.per_page, {"entity": 1})

        response = CreditCards.objects().aggregate(pipeline)

        response = CreditCardsTableResponse(**default_paginate_schema(response, request.page, request.per_page))
        
        return response

    def get_all(self, request, context):
        auth_token = parser_context(context, 'auth_token')
        is_auth(auth_token, '04_credit_cards_get_all')
        card_credit = parser_all_object(CreditCards.objects.all())
        response = CreditCardsMultipleResponse(credit=card_credit)

        return response

    def get(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '04_credit_cards_get')
            card_credit = CreditCards.objects.get(id=request.id)
            card_credit = parser_one_object(card_credit)
            response = CreditCardsResponse(credit=card_credit)

            return response

        except CreditCards.DoesNotExist as e:
            not_exist_code(context, e)

    def save(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '04_credit_cards_save')
            credit_cards_object = MessageToDict(request)
            card_credit = CreditCards(**credit_cards_object).save()
            card_credit = parser_one_object(card_credit)
            response = CreditCardsResponse(credit=card_credit)

            return response

        except NotUniqueError as e:
            exist_code(context, e)

    def update(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '04_credit_cards_update')
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
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '04_credit_cards_delete')
            card_credit = CreditCards.objects.get(id=request.id)
            card_credit = card_credit.delete()
            response = CreditCardEmpty()

            return response

        except CreditCards.DoesNotExist as e:
            not_exist_code(context, e)

def start_creditcards_service():
    add_CreditCardsServicer_to_server(CreditCardsService(), grpc_server)
