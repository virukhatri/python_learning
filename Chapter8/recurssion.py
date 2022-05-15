
'''# number = int(input("Enter your number : \n"))
def factorial_i(number):
    fact=1
    for i in range(1,number+1):
     fact=fact*i
    return fact

f= factorial_i(5)
print(f)


def factorial_rec(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial_rec(n-1)

print(factorial_rec(6))

number = int(input("Enter your number: \n"))

for i in range(2,number-1):
    if(number%i==0):
        print("This is not even number", number)
        break
else:
        print("This is the even number", number)

n=3
for i in range (3):
    print("*" * (n-i))

def cms(inches):
    inc= inches*2.54
    return inc

print(cms(2))

def removesplit(name):
    newStr= name.replace("this","")
    return newStr.strip()

print(removesplit(" this is the right word or not  "))'''


