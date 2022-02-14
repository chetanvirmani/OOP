import CarClass as cc

drive = cc.Car("2016","Mazda6")

for x in range(5):
    drive.accelerate()
    print ("The current speed is:",drive.get_speed())

for x in range(5):
    drive.brake()
    print ("The current speed is:",drive.get_speed())

