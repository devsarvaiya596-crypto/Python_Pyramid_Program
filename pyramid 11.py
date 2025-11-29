no = int(input("enter no of rows = "))
for i in range(1, no + 1):
    num = 1
    for j in range(i):
        print(num, end="")
        num += 2       
    print()            