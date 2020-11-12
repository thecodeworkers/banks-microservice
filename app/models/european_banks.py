from mongoengine import Document, StringField, DecimalField, BooleanField

class EuropeanBanks(Document):
    bankName = StringField(min_length=2,max_length=100, required=True)
    swift = StringField(min_length=2,max_length=11, required=True, unique=True)
    iban = StringField(min_length=2,max_length=25, required=True)
    country = StringField(min_length=2,max_length=80, required=True)
    