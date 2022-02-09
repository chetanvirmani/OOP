import CoinClass as c
#import the class created in the file (The file name - CoinClass)
#We are not just importing the class, we are importin gthe whole file
#If the file is in a different location then the whole path will be required
#in front of import


# The main function.
def main():
       # Create an object from the Coin class.
       my_coin = c.Coin()   # this creates an instance called 'my_coin' of the class 'Coin()'

    #Coin is the name of the class in the other file (Coin)
    # Display the side of the coin that is facing up.
       #my-coin now belongs to the Coin object like "Blah" belongs to string

       print('This side is up:', my_coin.get_sideup())    # notice you do not have to supply the argument/parameter

       # Toss the coin.
       print('I am going to toss the coin ten times:')
       for count in range(10):
           my_coin.toss() #toss function under coin class
           
           # Display the side of the coin that is facing up.
           print('This side is up:', my_coin.get_sideup())

           


       

# Call the main function.

main()
