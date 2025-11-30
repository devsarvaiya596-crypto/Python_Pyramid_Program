no=int(input("enter the row =>"))
ABC=65
abc=97
m=34

for i in range (1,no+2,1):
    for j in range (1,i+1):
        if i==1:
            print(" ",j,end=" ")
        elif i==2:
            print(" ",chr(ABC),end=" ")
            ABC+=1
        elif i==3:
            print(" ",chr(abc),end=" ")
            abc+=1
        elif i==4:
            print("  !",end=" ")
        elif i==5:
            print(" ",chr(m),end=" ")
            
    print()