a="GeeksForGeeks"
l=len(a)
u=0
lw=0
for i in range(l):
	if a[i]==a[i].upper():
			u+=1
	else:
			lw+=1
print("count of lowercase characters is:",lw)
print("count  of uppercase characters is:",u)
