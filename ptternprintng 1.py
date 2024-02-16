#pattern printng 1#
#1 2 3


l=int(input("enter the lines"))
for i in range(l+ 1):
    for j in range(1, i + 1):
        print(j, end="  ")
    print()
