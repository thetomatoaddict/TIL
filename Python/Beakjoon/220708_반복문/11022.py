a=int(input())
for i in range(a):
	b,c=map(int,input().split())
	print('Case #%d: %d + %d = %d'%(i+1,b,c,b+c))
