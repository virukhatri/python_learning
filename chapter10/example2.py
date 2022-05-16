'''with open("/Users/virenderkhatri/Desktop/Python_Program/Chapter1/chapter10/testdon.txt","r") as f:
    data=f.read()
    
data=data.replace("donkey","######")
    

with open("/Users/virenderkhatri/Desktop/Python_Program/Chapter1/chapter10/testdon.txt","w") as f:
    f.write(data)

words= ["viru","virender","khatri"]
with open("/Users/virenderkhatri/Desktop/Python_Program/Chapter1/chapter10/testdon.txt","r") as f:
    data=f.read()

for word in words:    
    data=data.replace(word,"######")
    

with open("/Users/virenderkhatri/Desktop/Python_Program/Chapter1/chapter10/testdon.txt","w") as f:
    f.write(data)

with open("/Users/virenderkhatri/Desktop/Python_Program/Chapter1/chapter10/log.txt") as f:
    data=f.read()

if "python" in data.lower():
    
    print("yes python is there")
else:
    print("no python is not there")

data=True
i=1
with open("/Users/virenderkhatri/Desktop/Python_Program/Chapter1/chapter10/log.txt") as f:
    while data:
        data=f.readline()

        if "python" in data.lower():
           print("yes python is there")
           print(i)
        i+=1
    

with open("/Users/virenderkhatri/Desktop/Python_Program/Chapter1/chapter10/this.txt") as f:
    data= f.read()

with open("copy.txt","w") as f:
    f.write(data)

with open("/Users/virenderkhatri/Desktop/Python_Program/Chapter1/chapter10/this.txt") as f:
    data1= f.read().lower()

with open("/Users/virenderkhatri/Desktop/Python_Program/Chapter1/copy.txt") as f:
    data2= f.read().lower()

if data1==data2:
    print("all data is matching")
else:
    print("data is not matching")

with open("/Users/virenderkhatri/Desktop/Python_Program/Chapter1/copy.txt","w") as f:
    f.write()
'''

import os


oldname="/Users/virenderkhatri/Desktop/Python_Program/Chapter1/chapter10/this.txt"
newname="rename_by_python.txt"

with open(oldname) as f:
    data=f.read()

with open(newname,"w") as f:
    f.write(data)

os.remove(oldname)
