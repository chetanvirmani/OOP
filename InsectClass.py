
import random

class Insect:

    def __init__(self,wings,legs):
        self.wings = wings
        self.legs = legs
        self.getflight = 2
    
    def fly(self):
        self.getflight = random.randint(1,10)
    
    def flyHigh(self):
        return self.getflight