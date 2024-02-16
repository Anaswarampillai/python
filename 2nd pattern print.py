#2nd pattern rintng

l=int(input("enter the line"))
# outer loop
for i in range(1, l+ 1):
    # inner loop
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
