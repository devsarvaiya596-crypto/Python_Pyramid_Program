no=int(input("enter the row =>"))
n=1
o=1

for i in range(no, 0, -1):
    for j in range(no- i):
        print(" ", end="")
    for k in range(1, i + 1):
         if o%2==0:
            print("#",end="")
            o+=1
         else :
            print("",n, end=" ")
            n+=2
            o+=1
    n=1
    o=1
    print() 