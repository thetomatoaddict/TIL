h,w,b = map(int,input().split())
n=h*w*b
print('%.2f'%round((n/8/1024/1024),2),'MB')