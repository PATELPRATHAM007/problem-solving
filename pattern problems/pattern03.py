inputNumber = int(input("enter any number"))

for i in range(5):
    for j in range(i+1):
        print(inputNumber,end="")
    inputNumber -= 1
    print("")

inputNumber += 1

for i in range(5):
    inputNumber += 1
    for j in range(5 - 1 - i):
        print(inputNumber,end="")
    print("")


    

    
