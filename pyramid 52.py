no=int(input("enter the row"))

for i in range (1,no+2,1):
    for j in range (no+1-i):
        print(" ",end="")
    for k in range(1,i):
        print("*",end=" ")
    print()
for a in range(no-1,0 , -1):
    for b in range(no-a):
        print("", end=" ")
    for c in range(1,a + 1):
        print("*",end=" ")
    print() 