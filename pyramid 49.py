no=int(input("enter limit =>"))

for i in range(no,0,-1):
	for j in range(i,0,-1):
		if i% 2 == 0:
			print(" #",end=" ")
		else:
			print(" *",end=" ")
	print()