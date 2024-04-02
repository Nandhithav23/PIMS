import Medicines
from dataclasses import dataclass


@dataclass
class Inventory:
    __inventory: list = None

    def add_med(self, name):
        self.__inventory.append(name)

    def remove_med(self, name):
        for medicine in self.__inventory:
            if name == medicine:
                self.__inventory.remove(name)
                print(f'{name} is removed successfully from the inventory')
                return
            else:
                print(f'{name} is not found')

    #@property
    #def getInventory(self): return self.__inventory
