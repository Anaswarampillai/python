## pttrn prntng 

#python code to print Pyramid of Incremental Numbers till the End in Python

l=6
n=1
for i in range (1,l+1):
    for j in range(i):
        print(n, end="  ")
        n+=1
    print()
