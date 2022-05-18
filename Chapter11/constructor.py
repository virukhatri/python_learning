class School:
    def __init__(self,name,secondName,lastName):
        self.name=name
        self.secondName=secondName
        self.lastName=lastName
    
    def printData(self):
        print(f"Name of the Employee is {self.name}")
        print(f"Second Name of the Employee is {self.secondName}")
        print(f"Last Name of the Employee is {self.lastName}")

viru=School("viru","virender","khatri")

viru.printData()