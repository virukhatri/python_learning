'''for i in range(5):
    try:
        print(i/0)
    except ZeroDivisionError as e:
        print(e, "---->>> Division by 0 is not possible")


for i in range(5):
    try:
        print(i/0)
    except ZeroDivisionError as e:
        print(e,"zero divided error")
    except NameError:
        print("name error")
    else:
        print("all is good no error is there")
    finally:
        print("i am pretty good")
else:
        print("outside the loop if all is good there")'''


import math
print(dir(math))
math.pi
print(math.sqrt(2))

