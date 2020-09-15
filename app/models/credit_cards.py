from mongoengine import Document, StringField, DecimalField, IntField,DateTimeField 

class CreditCards(Document):
    entity = StringField(max_length=100, required=True)
    cvcValidation = IntField(max_length=1, required=True)
    numberValidation = IntField(max_length=2, required=True)
    regex = StringField(required=True)