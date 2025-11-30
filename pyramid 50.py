no= int(input("Enter limit => "))
n=1
for i in range(no,0,-1):
    for j in range((no-i)*2):
        print(" ", end="")
    for k in range(i):
    	if i%2==0:
           print("#",end=" ")	
    	else:
           print("*",end=" ")	
    n=n+1
    print( )