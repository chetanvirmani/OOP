import CellPhoneClass as c

def main ():

    manuName = input ("Please enter the manufacturer's name: ")
    model = input("Please enter the Cell Phone Model: ")
    price = input("Please enter the Retail price: ")

    cellInfo = c.CellPhone(manuName,model,price)

    print(cellInfo.get_manufact())
    print(cellInfo.get_model())
    print(cellInfo.get_retail_price())

main()