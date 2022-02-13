from datetime import date


class student:

    def __init__(self,studentID,name,DateOfBirth,classification):
        self.__studentID = studentID
        self.__name = name
        self.__DateOfBirth = DateOfBirth
        self.__classification = classification
        self.__age = 0
        self.__registration = 0

    def studentAge(self):
        self.__age = date.today().year - self.__DateOfBirth.year - 1
    
    def registerationPeriod(self):

        if self.__classification == "F":
            self.__registration = "4/10 thru 4/12"
        elif self.__classification == "S":
            self.__registration = "4/7 thru 4/9"
        elif self.__classification == "Jr":
            self.__registration = "4/4 thru 4/6"
        elif self.__classification == "Sr":
            self.__registration = "4/1 thru 4/3"


    def getAge(self):
        return self.__age
    
    def getRegistration(self):
        return self.__registration


