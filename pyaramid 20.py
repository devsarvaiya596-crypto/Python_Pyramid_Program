no = int(input("enter no of rows = "))
for i in range(no):
    print(" " * i, end="")
    for j in range(1, no - i + 1):
        print(j, end=" ")  
    print()