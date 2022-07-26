tc=int(input())

for i in range(tc):
    print(f'#{i+1}')
    temp=[]
    cnt=0
    fc=int(input())
    for j in range(fc):
        a,b=map(str, input().split())
        for k in range(int(b)):
            temp.append(a)
        cnt+=int(b)
    for j in range(0,cnt,10):
        print(*temp[j:j+10],sep='')

