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

'''

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