
class CellPhone:

    def __init__(self,manu,model,price):
        self.__manufact = manu
        self.__model = model
        self.__retail_price = price
    
    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price
