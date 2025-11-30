no=int(input("enter the row =>"))
n=no*2


for i in range(no, 0, -1):
    for j in range(no- i):
        print(" ", end="")
    for k in range(1, i + 1):
        if n%2==0:
            print(n-1, end=" ")
        else :
            print(n, end=" ")
    n-=2
    print() 