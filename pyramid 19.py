no = int(input("enter no of rows = "))
for i in range(no, 0, -1):
    print(" " * (i - 1), end="")
    for j in range(i, no + 1):
        print(j, end=" ")
    print()