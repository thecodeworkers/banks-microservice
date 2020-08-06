from mongoengine import Document, StringField, DecimalField, BooleanField

BANK_TYPE = ('saving', 'current')

class Banks(Document):
    bank_name = StringField(max_length=100, required=True)
    user_name = StringField(max_length=100, required=True)
    routing_number = StringField(max_length=9, min_length=9)
    swift = StringField(max_length=12, max_length=12)
    number_account = StringField(max_length=20,min_lengtrequired=True)
    iban = StringField(max_length=4, min_length=4)
    type_account = StringField(max_length=10, choices=BANK_TYPE)
    address = StringField()
    document_identification = StringField()