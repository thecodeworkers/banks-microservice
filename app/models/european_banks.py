from mongoengine import Document, StringField, DecimalField, BooleanField

class EuropeanBanks(Document):
    bankName = StringField(max_length=100, required=True)
    swift = StringField(max_length=11, required=True, unique=True)
    iban = StringField(max_length=4, required=True)
    country = StringField(max_length=80, required=True)
    