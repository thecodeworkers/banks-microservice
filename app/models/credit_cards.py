from mongoengine import Document, StringField, DecimalField, IntField,DateTimeField 

class CreditCards(Document):
    cardNumber = StringField(max_length=16, required=True)
    username = StringField(max_length=100, required=True)
    cvc = StringField(max_length=4, required=True)
    expiration = StringField(required=True)
    documentIdentification = StringField(required=True)