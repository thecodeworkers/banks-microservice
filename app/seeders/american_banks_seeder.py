from ..models import AmericanBanks
from ..settings import Database

def american_bank_seeder():
    database = Database()
    database.start_connection()

    datas = [
        {
            'bankName':"Bank of America",
            'routingNumber': "012345678",
            'swift': "BOFAUS3N"
        },
        {
            'bankName':"Chase Bank",
            'routingNumber': "012345679",
            'swift': "CHASUS33"
        },
        {
            'bankName':"Citi Bank",
            'routingNumber': "012345670",
            'swift': "CITIUS33"
        }
    ]

    for data in datas:
        exist_american = AmericanBanks.objects(swift=data['swift'])
        if not exist_american: AmericanBanks(**data).save()
    
    database.close_connection()