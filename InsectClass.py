
import random

class Insect:

    def __init__(self):
        self.wings = 2
        self.legs = 4
        self.getflight = 2
    
    def fly(self):
        self.getflight = random.randint(1,10)
        return self.getflight