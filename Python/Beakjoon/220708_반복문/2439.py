a=int(input())
n=a
for i in range(a):
	print(' '*(n-1),'*'*(i+1),sep="")
	n=n-1
