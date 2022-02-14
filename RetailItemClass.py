
class Retail:

    def __init__(self,itemDescription,unitsInInventory,price):

        self.__itemDescription = itemDescription
        self.__unitsInInventory = unitsInInventory
        self.__price = price
    
    def get_itemDescription(self):
        return self.__itemDescription
    
    def get_unitsInInventory(self):
        return self.__unitsInInventory
    
    def get_price(self):
        return self.__price
