from mongoengine import Document, StringField, DecimalField, IntField,DateTimeField 

class CreditCards(Document):
    entity = StringField(min_length=2,max_length=100, required=True)
    cvcValidation = IntField(min_length=1,max_length=1, required=True)
    numberValidation = IntField(min_length=1,max_length=2, required=True)
    regex = StringField(min_length=2,required=True)