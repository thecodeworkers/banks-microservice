from mongoengine import Document, StringField, DecimalField, BooleanField

class LatinAmericanBanks(Document):
    bankName = StringField(max_length=100, required=True)
    swift = StringField(max_length=11, required=True, unique=True)
    country = StringField(max_length=80, required=True)
    