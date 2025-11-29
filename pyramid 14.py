no = int(input("enter no of rows = "))

n = 2 * no - 1

for i in range(no):
    num = n
    for j in range(no - i):
        print(num, end="")
        num -= 2
    print()
    n -= 2