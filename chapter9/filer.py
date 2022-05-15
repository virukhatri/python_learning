#/Users/virenderkhatri/Desktop/Python_Program/Chapter1/chapter9/sample1.txt
import os
f = open('/Users/virenderkhatri/Desktop/Python_Program/Chapter1/chapter9/sample.txt')
#f=open("sample.txt","w")
#data = f.read()
data=f.readline()
print(data)
data=f.readline()

print(data)
f.close()