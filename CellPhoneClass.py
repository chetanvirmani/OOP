
class CellPhone:

    def __init__(self,manu,model,price):
        self.__manufact = manu
        self.__model = model
        self.__retail_price = price
    
    def set_manufact(self,manu):
        self.__manufact = manu
        return self.__manufact

    def set_model(self,model):
        self.__model = model
        return self.__model

    def set_retail_price(self, price):
        self.__retail_price = price
        return self.__retail_price
