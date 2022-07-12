a,b,c=map(int,input().split())

if a==b==c:
	print(a*1000+10000)
elif a==b:
	print(a*100+1000)
elif b==c:
	print(b*100+1000)
elif a==c:
	print(a*100+1000)
elif a>b>c or a>c>b:
	print(a*100)
elif b>a>c or b>c>a:
	print(b*100)
elif c>a>b or c>b>a:
	print(c*100)
	
