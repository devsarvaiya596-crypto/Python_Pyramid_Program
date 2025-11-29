row= int(input("Enter limit => "))
a=48
for i in range(row):
    for j in range(i+1):
        alpha=chr(a)
        print(alpha, end="")
    a+=1
    print("")