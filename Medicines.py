from dataclasses import dataclass
import datetime


@dataclass
class Medicines:
    __name: str
    __expiry: datetime.date
    __price: float = None
    __quantity: int = None
    __category: str = None

    @property
    def get_name(self): return self.__name

    @property
    def get_expiry(self): return self.__expiry

    @property
    def get_price(self): return self.__price

    @property
    def get_quantity(self): return self.__quantity

    @property
    def get_category(self): return self.__category

    def display_info(self):
        return {
            'Name': self.__name,
            'Category': self.__category,
            'Expiry': self.__expiry.strftime('%d %B %Y'),
            'Price': self.__price,
            'Quantity': self.__quantity
        }


med = Medicines('Paracetamol', datetime.date(2024, 8, 23), 89, 9, 'Fever')
print(med.display_info())
