symbolList = ["@","#","$","%","&"]

for i in range(5):
    for j in range(5-i-1):
        print(" ",end="")
    for k in range(i,-1,-1):
        print(symbolList[k],end="")

    print("")
