h,b,c,s = map(int,input().split())
n=h*b*c*s
print(round((n/8/1024/1024),1),'MB')