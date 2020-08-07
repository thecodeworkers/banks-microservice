from mongoengine import Document, StringField, DecimalField, BooleanField

BANK_TYPE = ('saving', 'current')

class Banks(Document):
    routing_number = StringField(max_length=9, min_length=9)
    bank_name = StringField(max_length=100, required=True)
    full_name = StringField(max_length=100, required=True)
    swift = StringField(min_length=11, max_length=11)
    number_account = StringField(max_length=20,min_length=20, required=True)
    type_account = StringField(max_length=10, choices=BANK_TYPE)
    user_address = StringField()
    document_identification = StringField()
    currency = StringField()

    