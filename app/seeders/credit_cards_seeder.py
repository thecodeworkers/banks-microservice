from ..models import CreditCards
from ..settings import Database

def credit_card_seeder():
    database = Database()
    database.start_connection()

    datas = [
        {
            'entity':"Bank of America",
            'cvcValidation': 3,
            'numberValidation': 16,
            'regex': "[0-9]?"
        },
        {
            'entity':"Chase Bank",
            'cvcValidation': 3,
            'numberValidation': 16,
            'regex': "[0-9]?"
        },
        {
            'entity':"Citi Bank",
            'cvcValidation': 3,
            'numberValidation': 16,
            'regex': "[0-9]?"
        }
    ]

    for data in datas:
        exist_credit = CreditCards.objects(entity=data['entity'])
        if not exist_credit: CreditCards(**data).save()
    
    database.close_connection()