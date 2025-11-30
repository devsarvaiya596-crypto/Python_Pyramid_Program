no= int(input("Enter limit => "))
n=no*2
for i in range(no,0,-1):
    for j in range((no-i)*2):
        print(" ", end="")
    for k in range(i):
    	if n%2==0:
           print(n-1,end=" ")	
           n-=2
    	else:
           print(n,end=" ")	
           n-=2
    n=no*2
    print( )