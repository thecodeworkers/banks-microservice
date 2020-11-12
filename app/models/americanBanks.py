from mongoengine import Document, StringField, DecimalField, BooleanField

BANK_TYPE = ('saving', 'current')

class AmericanBanks(Document):
    bankName = StringField(min_length=2,max_length=100, required=True) 
    routingNumber = StringField(min_length=2,max_length=9, required=True, unique=True)
    swift = StringField(min_length=2,max_length=11, required=True, unique=True)

