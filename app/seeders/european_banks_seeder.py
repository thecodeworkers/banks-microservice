from ..models import EuropeanBanks
from ..settings import Database

def european_bank_seeder():
    database = Database()
    database.start_connection()

    datas = [
        {
            'bankName':"Banco Santander",
            'swift': "BSCHESMM",
            'country': "Espana",
            'iban': 'ES9121000418450200051332'
        },
        {
            'bankName':"Millenium BCP",
            'swift': "BCOMPTPL",
            'country': "Portugal",
            'iban': 'PT50000201231234567890154'
        },
        {
            'bankName':"Ubi Banca",
            'swift': "BLOPIT22",
            'country': "Italia",
            'iban': 'none'
        }
    ]

    for data in datas:
        exist_european = EuropeanBanks.objects(swift=data['swift'])
        if not exist_european: EuropeanBanks(**data).save()
    
    database.close_connection()