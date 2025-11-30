no=int(input("enter limit =>"))
n=1
m=1
for i in range(1,no+1):
	for j in range(1,i+1):
		if n%2==0:
			print("  #",end=" ")
			n+=1
		else:
			print("",m,end=" ")
			m=m+2
			n=n+1
	n=1
	m=1
       
	print()