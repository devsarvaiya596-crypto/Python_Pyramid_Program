no=int(input("enter limit =>"))

for i in range(1,no+1):
	for j in range(1,i+1,1):
		if i% 2 == 1:
			print(" $",end=" ")
		else:
			print(" @",end=" ")
	print()