from mongoengine import Document, StringField, DecimalField, BooleanField

BANK_TYPE = ('saving', 'current')

class Banks(Document):
    id = StringField()
    routingNumber = StringField()
    bankName = StringField(max_length=100, required=True)
    fullName = StringField(max_length=100, required=True)
    swift = StringField()
    numberAccount = StringField(required=True)
    type = StringField(max_length=10, choices=BANK_TYPE)
    # user_address = StringField()
    # document_identification = StringField()
    currency = StringField()

    

    