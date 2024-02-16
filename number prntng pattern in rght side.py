#number printng in pattern in right side
for i in range(0,5):
    for j in range(5,0,-1):
        if j>i+1:
            print(" " ,end=" ")
        else:
            print(j,end=" ")
    print()
