level = int(input("enter any number : "))

for i in range(level):
    number = 1 
    for j in range(i+1):
        print(number,end="")
        number += 1

    for k in range((2*level) - 2*(i+1)):
        print(" ",end="")

    number -= 1
    for l in range(i+1):
        print(number,end="")
        number -= 1
    print("")