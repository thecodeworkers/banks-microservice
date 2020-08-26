from mongoengine import Document, StringField, DecimalField, BooleanField

BANK_TYPE = ('saving', 'current')

class AmericanBanks(Document):
    routingNumber = StringField(max_length=9, required=True)
    bankName = StringField(max_length=100, required=True)
    fullName = StringField(max_length=100, required=True)
    swift = StringField(max_length=11, required=True)
    ach = StringField()
    numberAccount = StringField(required=True)
    type = StringField(max_length=10, choices=BANK_TYPE, required=True)
    documentIdentification = StringField(required=True)
    currency = StringField(required=True)
