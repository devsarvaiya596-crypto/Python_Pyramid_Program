rows=int(input("enter no of rows"))
a=65
for i in range (rows,0,-1):
	for j in range (i,0,-1):
		alpha =chr(a)
		print("",alpha,end="")
		a+=1
		
	a=65
	print()