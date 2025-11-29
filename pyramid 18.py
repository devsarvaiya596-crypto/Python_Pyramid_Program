no = int(input("enter no of rows = "))
for i in range(1, no + 1):
    print(" " * (no - i), end="")
    for j in range(i, 0, -1):
        print(j, end=" ")   
    print()