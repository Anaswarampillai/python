#string palindrome checking

a=str(input("enter the string"))
rev=""
for i in a:
  rev=i+rev
if a==rev:
  print("the string is palindrome")
else:
    print("the string is not a palindrome")
    
