from mongoengine import Document, StringField, DecimalField, IntField,DateTimeField 

class CreditCard(Document):
    card_number = IntField(max_length=9, min_length=9 required=True)
    username = StringField(max_length=100, required=True)
    cvc = IntField(max_length=4, min_length=3, required=True)
    expiration = DateTimeField(required=True)
    document_identification = IntField()