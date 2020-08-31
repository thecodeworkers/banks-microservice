from .american_banks import start_americanbanks_service
from .credit_cards import start_creditcards_service
from .european_banks import start_europeanbanks_service

def start_all_servicers():
    start_americanbanks_service()
    start_creditcards_service()
    start_europeanbanks_service()


def start_all_emiters():
    # start_american_banks_emit()
    pass
