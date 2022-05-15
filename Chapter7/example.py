'''number = int(input("Enter your number : \n"))

i=1

while i<=10:
    number1=number*i
    i=i+1
    print(number1)

for i in range(1,11):
    print(i*number)

l1=["Harry","Saham","Sachin","Rahul"]

for name in l1:
    if(name.startswith("S")):
        print("Start with S : ",name)
    
number = int(input("enter the number : \n"))

for i in range(2,number):
    if number%i==0:
     print("This is the not the Prime Number : ",number)
     break
else:
        print("This is the Prime Number", number)

n=int(input("Enter your number : \n"))
i=1
sum=0
while i <= n:
    sum=sum+i
    i=i+1
print(sum)

number = int(input("Enter Your Number : \n"))
fact=1
for i in range(1,number+1):
    fact=fact*i
    
print("factorial value is = ",fact)

for i in range(1,4):
    print("*" *(i))

n=3
for i in range(3):
    print(" " * (n-i-1), end="")
    print("*" * (i*2+1), end="")
    print(" " * (n-i-1))
    

n=3
for i in range(3):
    print("*" , end="")
    print("*" * (n-i-2), end="")
    print("*")
    '''

number = int(input("Enter your number : \n"))
'''
i=1

while i<=10:
    number1=number*i
    i=i+1
    print(number1)
lst=[]
for i in range(10,0,-1):
    print(i*number)    '''  
lst=[] 
print(type(lst))        
for i in range(1,11):
    apn=i*number
    lst.append(apn)
lst.reverse()
print(lst)
    



