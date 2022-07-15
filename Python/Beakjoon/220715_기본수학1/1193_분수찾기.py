x=int(input())
l=1
while x-l > 0:
    x-=l
    l+=1


if l%2 == 0 :
    l=l-x+1
    print(x,"/",l,sep='')
else :
    l=l-x+1
    print(l,"/",x,sep='')

