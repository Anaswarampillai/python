basic_sal=float(input("enter the basic salary of a person : "))
percentage_of_allownce=float(input("enter the percentage of allowaance: "))
percent_of_dedctn=float(input("enter the percentage of deduction:" ))
net_sal =basic_sal + (basic_sal*percentage_of_allownce/100) - (basic_sal * percent_of_dedctn/100)
print("the net sal5ary is : ",net_sal)