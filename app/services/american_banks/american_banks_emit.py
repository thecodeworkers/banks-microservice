from ...utils import parser_all_object
from ...models import AmericanBanks
from ..bootstrap import service_bus

class AmericanBanksEmitter():
    def __init__(self):
        self.__start_emitters()

    def emit_american_banks(self):
        service_bus.add_queue('americans', self.__get_all_american_banks)

    def emit_american_bank(self):
        service_bus.add_queue('american', self.__get_one_american_bank)

    def __get_all_american_banks(self):
        us_banks = parser_all_object(AmericanBanks.objects.all())
        return us_banks

    def __get_one_american_bank(self):
        us_bank = self.__get_all_american_banks()[0]
        return us_bank

    def __start_emitters(self):
        self.emit_american_banks()
        self.emit_american_bank()

def start_american_banks_emit():
    AmericanBanksEmitter()
    service_bus.send()
