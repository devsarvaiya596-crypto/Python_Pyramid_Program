no=int(input("enter the row =>"))
n=1
m=1

for i in range(no, 0, -1):
    for j in range(no- i):
        print(" ", end="")
    for k in range(1, i + 1):
        print(n, end=" ")
        n+=1
    n=1
    n+=m
    m+=1
    print() 