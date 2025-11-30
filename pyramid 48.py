no=int(input("enter the row =>"))

for i in range(no, 0, -1):
    for j in range(no- i):
        print(" ", end="")
    for k in range(1, i + 1):
         if i%2==0:
            print(" #",end="")
         else :
            print(" *",end="")
    print() 