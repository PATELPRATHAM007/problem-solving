import string 
capitalLetters = list(string.ascii_uppercase)
inputLetter = input("enter any one letter : ")
capitalizeInputLetter = inputLetter.capitalize()
positionOfInputLetter = capitalLetters.index(capitalizeInputLetter)
n = positionOfInputLetter + 1
space = 0

for i in range(n):
    if i == 0:
        for j in range(2*n):
            print(capitalLetters[i],end="")
    else:
        for j in range(((2*n)//2) - i):
            print(capitalLetters[i],end="")
        
        for k in range(space):
            print(" ",end="")
        
        for l in range(((2*n)//2) - i):
            print(capitalLetters[i],end="")
        
    space += 2
    print("")


            






'''
aaaaaaaaaa
bbbb  bbbb
ccc    ccc
dd      dd
e        e

'''