import random

# The Coin class simulates a coin that can
# be flipped.

#This is a class (The name of the class needs to have
# the first letter to be upper case)
class Coin:
    # The _ _init_ _ method initializes the
    # sideup data attribute with 'Heads'.

#Init method initializes
    def __init__(self):
        self.__sideup = 'Heads'
    #sideup is something that we came
    #up with
    #All our coins are starting with the head
    #up
    
    #self attribute (for example bullet, damage, defence)

    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
    # Randomly picking between 0 and 1
        else:
            self.__sideup = 'Tails' #Adding two underscores will make the attribute hidden (unchangable outside of the class file)

    # The get_sideup method returns the value
    # referenced by sideup.

    def get_sideup(self):
            return self.__sideup

    #sideup is the name that we came up with
    
