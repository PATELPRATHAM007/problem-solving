for i in range(5):
    for j in range(5 - 1 - i ):
        print(" ",end="")
    num = i
    for k in range(i+1):
        print(num+1,end="")
        num += 1

    num -= 1
    
    for l in range(i):
        print(num,end="")
        num -= 1
    print("")