num = 1
alpha = 65
m = 1

for i in range(1,4):
	for j in range(1,i+1):
		if num% 2 == 0:
			print(chr(alpha),end="")
			alpha=alpha+1
			num = num+1
		else:
			print(m,end="")
			m=m+1
			num=num+1
	print()