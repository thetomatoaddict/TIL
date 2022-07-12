a,b=map(int,input().split())
c=list(map(int,input().split()))

for i in range(a):
	if int(c[i]) < b:
		print(c[i],end=' ')
		
