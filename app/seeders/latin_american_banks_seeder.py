from ..models import LatinAmericanBanks
from ..settings import Database

def latin_american_bank_seeder():
    database = Database()
    database.start_connection()

    datas = [
        {
            'bankName':"Banesco",
            'swift': "UNIOVECA",
            'country': "Venezuela"
        },
        {
            'bankName':"Mercantil",
            'swift': "BAMRVECA",
            'country': "Venezuela"
        },
        {
            'bankName':"Provincial",
            'swift': "BPROVECA",
            'country': "Venezuela"
        }
    ]

    for data in datas:
        exist_latin = LatinAmericanBanks.objects(swift=data['swift'])
        if not exist_latin: LatinAmericanBanks(**data).save()
    
    database.close_connection()