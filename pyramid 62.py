no=int(input("enter limit =>"))
n=1
for i in range(1,no+1):
    for j in range(1,i+1):
        print("",n*n*n,end="")
        n+=1
    print("")