from mongoengine import Document, StringField, DecimalField, BooleanField

BANK_TYPE = ('saving', 'current')

class EuropeanBanks(Document):
    bankName = StringField(max_length=100, required=True)
    fullName = StringField(max_length=100, required=True)
    swift = StringField(max_length=11, required=True)
    iban = StringField(max_length=4, required=True)
    currency = StringField(required=True)
    numberAccount = StringField(max_length=20, required=True)
    bankAddress = StringField(max_length=100, required=True)
    userAddress = StringField(max_length=100, required=True)
    type = StringField(max_length=10, choices=BANK_TYPE, required=True)
    documentIdentification = StringField(required=True)
