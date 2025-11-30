no=int(input("enter the row"))

for i in range(no,1, -1):
    for j in range(no- i):
        print(" ", end="")
    for k in range(1, i + 1):
        print("*", end=" ")
    print()b
for i in range (1,no+2,1):
    for j in range (no+1-i):
        print(" ",end="")
    for k in range(1,1*i):
        print("*" ,end=" ")
    print()