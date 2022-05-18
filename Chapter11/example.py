'''class Remote:
    def isLeftPressed(self):
        pass
    def isRightPressed(self):
        pass
    def isTopPressed(self):
        pass
    def isBelowPressed(self):
        pass

class Player:

    def moveRight(self):
        pass
    def moveLeft(self):
        pass
    def moveTop(self):
        pass
    def moveBelow(self):
        pass

player1=Player()
remote1= Remote()

if (remote1.isLeftPressed()):
    player1.moveLeft()
elif (remote1.isRightPressed()):
    player1.moveRight()
elif (remote1.isTopPressed()):
    player1.moveTop()
elif (remote1.isBelowPressed()):
    player1.moveBelow()



class Employee:
    company = "Google"
    projectName =""


viru = Employee()
viru1 = Employee()
print(viru.company)
print(viru1.company)
viru.company="Youtube"
print(viru.company)
print(viru1.company)
Employee.company="Youtube"
print(viru.company)
print(viru1.company)
viru.salary=5000000

print(viru.salary)
viru.projectName="Python"
print(viru.projectName)

class Programmer:
    company ="Microsoft"
    
    def __init__(self,name,designation,address,blood_group):
        self.name=name
        self.designation=designation
        self.address=address
        self.blood_group=blood_group

    def getDetails(self):
        print(f"Name is {self.name}, designation is {self.designation}, Address is {self.address}, and blood group is {self.blood_grou}")

viren=Programmer("Virender","Lead Conslultant","599/1,Jatwara,Sonipat","A+")
viren.getDetails()

from cmath import sqrt
from numpy import number
from pyparsing import null_debug_action


class Calculator:

    def __init__(self,number):
        self.number=number
    
    @staticmethod
    def greet():
        print("hello")

    def square(self):
        sqre=(self.number **2)
        print(f"Square of the given number is {sqre}")

    def cube(self):
        cub=(self.number **3)
        print(f"Square of the given number is {cub}")

    def squareroot(self):
        sqr=(self.number **0.5)
        print(f"Square of the given number is {sqr}")

sq=Calculator(2)
sq.square()
sq.cube()
sq.squareroot()
sq.greet()

class Attribute:
    a=10

obj=Attribute()
obj.a=0
print(obj.a)
print(Attribute.a)
Attribute.a=40
print(Attribute.a)


class Train:

    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats

    def bookTicket(self):
        length=len(self.seats)
        if (length>0):
            bookedSheet=self.seats.pop()
            print(f"Your ticket is booked & Your sheet number is {bookedSheet}")
            
        else:
            print("Sorry, Ticket is not available")
    def getStatus(self):
        print(f"Name of the train is {self.name}")
        print(f"Seats of the train is {self.seats}")
    def getFare(self):
        print(f"Fare information of the train is {self.fare} rupees")

    
    def cancelTicket(self,seatNumber):
            print(f"Your Request for cancelled ticket is approved and your {seatNumber} is cancelled")
            self.seats.add(seatNumber)
    


obj=Train("Stabhadi: 17678", 5000, {1,2})

obj.getStatus()
obj.bookTicket()
obj.getFare()
obj.bookTicket()
obj.cancelTicket(1)
obj.bookTicket()

'''