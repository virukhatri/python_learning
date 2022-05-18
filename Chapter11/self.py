class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary is 4800 Pay Grade and salary is {self.salary} and company is {self.company}")

viru= Employee()
viru.salary=160000
viru.getSalary() # Employee.getSalary(viru)
