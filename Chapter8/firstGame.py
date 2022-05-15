import random

print("Computer: Enter Snake(s), Water(w) or Gun(g)")
randNo= random.randint(1,3)
if(randNo==1):
    comp="s"
elif(randNo==2):
    comp="w"
elif(randNo==3):
    comp="g"


you=input("Enter Snake(s), Water(w) or Gun(g) ")



def firstGame(comp,you):
    if(comp==you):
        return None
    elif(comp=="s"):
        if(you=="w"):
            return False
        elif(you=="g"):
            return True
    elif(comp=="w"):
        if(you=="s"):
            return True
        elif(you=="g"):
            return False
    elif(comp=="g"):
        if(you=="w"):
            return True
        elif(you=="s"):
            return False


value=firstGame(comp,you)
print(comp,you)
if value==None:
    print("Game is Tie!")
elif value==True:
    print("I win the Game")
elif value==False:
    print("I lost the Game")
    