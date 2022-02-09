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
        self.sideup = 'Heads'
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
            self.sideup = 'Heads'
    # Randomly picking between 0 and 1
        else:
            self.sideup = 'Tails'

    # The get_sideup method returns the value
    # referenced by sideup.

    def get_sideup(self):
            return self.sideup

    #sideup is the name that we came up with
    
