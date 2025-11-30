n=int(input("Enter row limit =>"))
for i in range(1,n+1,1):
    for j in range(1,i+1):
        if j<5:
           print("",j,end="")
    for k in range(1,2*(n-i),1):
        print(" ",end=" ")
    for l in range(i,0,-1):
        print("",l,end="")
    print()