#print * in pattern prgrm
l=int(input("enter the line"))
for i in range(l):
    for j in range(1,i+1):
        print("*",end="  ")
        print("+",end="  ")
    print()
