no=int(input("enter no of rows =>"))
for i in range (no):
	for j in range (i):
		if i==1:
		    print("",chr(92),end="")
		if i==2:
		    print("",chr(39),end="")
		if i==3:
		     print("",chr(126),end="")
		if i==4:
		     print("",chr(61),end="")
		if i==5:
		     print("",chr(62),end="")
	print()