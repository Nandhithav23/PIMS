from Medicines import Medicines
from dataclasses import dataclass, field
import datetime

@dataclass
class Inventory:
    __medicines: list[Medicines] = field(default_factory=list)  # Private list

    def add_med(self, name: str, expiry: datetime.date, price: float, quantity: int, category: str):
        med = Medicines(name, expiry, price, quantity, category)
        self.__medicines.append(med)

    def search_and_remove_med(self, remove=False, **kwargs):
        med_found = [med for med in self.__medicines if
                     all(getattr(med, f'_Medicines__{key}') == value for key, value in kwargs.items())]
        if med_found:
            print(f'Medicine(s) with the given criteria found in the inventory')
            for med in med_found:
                print(med.display_info())

            if remove:
                self.__medicines = [med for med in self.__medicines if med not in med_found]
                print(f'Medicine(s) removed successfully from the inventory')
            return
        print(f'No medicine found matching the criteria')

    def update_quantity(self, name: str, new_q: int):
        for med in self.__medicines:
            if med._Medicines__name == name:  # Accessing private attribute directly
                med._Medicines__quantity = new_q  # Updating private attribute directly
                print(f'Quantity of {name} is updated successfully')
                return
        print(f'{name} is not found in the inventory')

    def update_price(self, name: str, new_p: float):
        for med in self.__medicines:
            if med._Medicines__name == name:  # Accessing private attribute directly
                med._Medicines__price = new_p  # Updating private attribute directly
                print(f'Price of {name} is updated successfully')
                return
        print(f'{name} is not found in the inventory')

    def remove_expired_meds(self):
        today = datetime.date.today()
        expired = [med for med in self.__medicines if med._Medicines__expiry < today]
        if expired:
            print('\nRemoving expired medicines from the inventory --')
            for med in expired:
                print(med.display_info())
            self.__medicines = [med for med in self.__medicines if med not in expired]
            print('Expired medicines removed successfully')
        else:
            print('No expired medicines found in the inventory')

    def display_inventory(self):
        if not self.__medicines:
            print('No medicines found--Zero Stock')
            return
        print('\n\nINVENTORY: ')
        for med in self.__medicines:
            print(med.display_info())
        print()


inventory = Inventory()

# Adding into the inventory
inventory.add_med('Dolo', datetime.date(2024, 11, 25), 10.4, 3, 'Fever')
inventory.add_med('Panadol', datetime.date(2024, 4, 9), 5.6, 2, 'Painkiller and Fever')

inventory.display_inventory()

# Updating price and quantity
inventory.update_price('Dolo', 8.9)
inventory.update_quantity('Panadol', 6)

inventory.display_inventory()

# Search (by the given criteria) and remove(if remove=True)
inventory.search_and_remove_med(False, category='Fever')

# Remove expired meds by checking the expiry dates
inventory.remove_expired_meds()

inventory.display_inventory()
