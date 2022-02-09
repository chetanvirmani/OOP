import InsectClass as ic


def main():

    flight = ic.Insect(2,4)

    flight.fly()

    print("The flight length is:", flight.flyHigh(), "miles.")

main()