h,m=map(int,input().split())

m=m-45 #10 10 -> 10 -35

if m<0:
	m=60+m # 10 -35 -> 10 25
	h=h-1 # 9 25
	if h<0:
		h=(h+24)
		print(h,m)
	elif h>=0:
		print(h,m)
elif m>=0:
	print(h,m)
