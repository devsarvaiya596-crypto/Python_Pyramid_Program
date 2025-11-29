no = int(input("enter no of rows = "))

k= 1  

for i in range(1, no + 1):
    num = k
    for j in range(i):
        print(num, end="")
        num -= 2      
    print()         
    k += 2        