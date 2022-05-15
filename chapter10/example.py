'''with open("poem.txt","r") as f:
    data=f.read()

  print(len(f.read()))
    print(f.seek(0))
    print(len(f.read()))
    f.truncate(13)

if "twinkle" in data:
    print("twinkle is present")
else:
    print("twinkle is not present")

import numbers
import random


def game():
    ran= random.randint(1,78)
    return ran

score=game()
print(score)
with open("poem.txt","r") as f:
    hiscore = f.read()

if hiscore==" ":
    with open("poem.txt","w") as f:
        f.write(str(score))
elif score > int(hiscore):
    with open("poem.txt","w") as f:
        f.write(str(score))'''

def multtable(start_range,end_range):
    for i in range(start_range,end_range):
        with open(f"tables/multiplication{i}","w") as f:
            for j in range(1,11):
                f.write(f"{i}X{j}={i*j}\n")
        
multtable(1,25)
        






    

