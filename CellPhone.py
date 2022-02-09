import CellPhoneClass as c

def main ():

    manuName = input ("Please enter the manufacturer's name: ")
    model = input("Please enter the Cell Phone Model: ")
    price = input("Please enter the Retail price: ")

    cellInfo = c.CellPhone(manuName,model,price)

    print(cellInfo.set_manufact(manuName))
    print(cellInfo.set_model(model))
    print(cellInfo.set_retail_price(price))

main()