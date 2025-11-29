no = int(input("enter no of rows = "))
for i in range(no):
    print(" " * i, end="")
    for j in range(no - i):
        print(no - i, end=" ")  
    print()