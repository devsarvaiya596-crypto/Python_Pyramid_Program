rows =int(input("enter the row =>"))
n=rows

for i in range(rows, 0, -1):
    for s in range(rows - i):
        print(" ", end="")
    for num in range(1, i + 1):
        print(n, end=" ")
        n-=1
    n=rows
    print() 