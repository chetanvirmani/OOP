import StudentClass as sc
from datetime import date

def main ():

    studentID = input ("Please enter your student ID: ")
    name = input ("Please enter your Name: ")

    print("Please enter your Birth Date: -")
    year = int(input("Year (yyyy): "))
    month = int(input("Month (mm): "))
    day = int(input("Day (dd): "))
    
    DateOfBirth  = date(year,month,day)
    classification = input ("Please enter your school year (F,S,Jr,Sr): ")

    studentDetails = sc.student(studentID,name,DateOfBirth,classification)

    studentDetails.studentAge()
    studentDetails.registerationPeriod()

    print ("The age of the student is:",studentDetails.getAge())
    print ("The applicable registration period for the student is:",studentDetails.getRegistration())


main()