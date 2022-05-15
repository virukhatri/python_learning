'''
def highest(n1,n2,n3):
    if(n1>n2):
        high=n1
    else:
        high=n2

    if(n3>high):
        high=n3
    return high

print(highest(12,29,29.2))

def cfformula(value):
    f=(value * 9/5) + 32
    return f

print(cfformula(50))

def sumRecur(number):
    if(number>0):
        return number + (sumRecur(number-1))
    else:
        return 0 
print(sumRecur(5))

def tableOfnumber(number):
    lst=[]
    for i in range(1,11):
        lst.append(i*number)
    return lst
    

print(tableOfnumber(4))

n=3
for i in range(3):
    print("*" * (n-i))
'''

