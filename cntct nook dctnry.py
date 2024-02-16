#contact book python dictionaryq

dic1={}
print("1. Add New Contact")
print("2. delete  of Contact")
print("3. edit or modify  a contact")
print("4.search a contact ")
print("5. Display all entries")
print("6. Exit")
while True:
 inp=int(input("Enter your choice: "))
if(inp==1):
  name = input("Enter your friend name: ")
  phonenumber = input("Enter your friend's contact number: ")
  dic1['name'] = phonenumber
  print("Contact Added ")
elif(inp == 2):
  name = input("Enter the name of friend whose contact is to be deleted: ")
  if(name in dic1):
    del dic1[name]
    print("Contact Deleted")
elif(inp==3):
    name = input("Enter the name of friend whose number is to be edit: ")
    if(name in dic1):
     phonenumber = input("Enter the new contact number: ")
     dic1[name] = phonenumber
     print("Contact edited")
elif(inp==4):
  name  = input("Enter the name of friend to search: ")
  if(name in dic1):
   print(name,"is present in the list")
elif(inp==5):
   print("All entries in the contact")
   for a in dic1:
    print(a,"\t\t",dic1[a])
elif(inp==6):
    
break
else:
 print("Invalid Choice")
