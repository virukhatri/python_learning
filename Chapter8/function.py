'''marks1=[76,67,89,78,76]
marks2=[88,56,86,78,98,67,87]
def percen(marks):
    percent =(sum(marks)/(len(marks)*100))*100
    return percent
print(percen(marks1))
print(percen(marks2))

def greet(name):
    print("Good Day "+name)
    
greet("Viru")


def mySum(n1,n2):
    return n1+n2
print(mySum(22,89))

# function with argument

def greets(names):
    newname="greeting " +names
    return newname

newString=greets("viren")
print(newString)


# default argument
def greets(names="Khatri"):
    newname="greeting " +names
    return newname

newString=greets("viren")
print(newString)

newString=greets()
print(newString)

n=3
for i in range(1,4):
    print("*", end="")
    if(i==(n-1)):
        print(" ", end="")
    else:
        print("*", end="")
    print("*")

number = int(input("Enter your number: \n"))
def primeNo(number):
    if(number==0 or number==1):
        return True
    for i in range(2,number-1):
        if(number%i==0):
            return False
    else:
        return True

a= primeNo(number)
if a==True:
    print(f"Given number is prime number and number is : {number}")
elif a==False:
    print(f"Given number is not prime number and number is : {number}")
else:
    print(f"not a valid input and number is : {number}")'''


def myFunc():
        print("This is my function")


myFunc()

def rangeingFun(x):
    for i in range(x):
        x-=x-i
        return i
    else:
        print("test")

    
