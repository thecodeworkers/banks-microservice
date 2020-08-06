from mongoengine import Document, StringField, DecimalField, IntField,DateTimeField 

CREDITCARD = ()

class CreditCard(Document):
    card_number = IntField(max_length=9, min_length=9 required=True)
    user_name = StringField(max_length=100, required=True)
    cvc = IntField(max_length=4, min_length=3)
    expiration = DateTimeField(required=True)
    document_identification = IntField(required=True)
