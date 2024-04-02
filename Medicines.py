from dataclasses import dataclass

@dataclass
class Medicines:
    __name:  str = None
    __expiry: str = None
    __price: float = None
    __quantity: int = None
    __category: str = None

    @property
    def getName(self): return self.__name
    @property
    def getExpiry(self): return self.__expiry
    @property
    def getPrice(self): return self.__price
    @property
    def getQuantity(self): return self.__quantity
    @property
    def getCategory(self): return self.__category



dolo = Medicines('29', 10.4, 3, 'Fever')
print(dolo.getPrice)  # Using getter

