#nested loop pattern printng

l=int(input("enter the line"))
for i in range(l):
  for j in range(l):
    print("*", end=" ")
  print()
