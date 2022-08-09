c,r=map(int, input().split())
parkingLot=[input() for _ in range(c)]
delta=[[0,0],[0,1],[1,0],[1,1]]
site0=0
site1=0
site2=0
site3=0
site4=0

for y in range(c-1):
    for x in range(r-1):
        tmp=''
        for d in delta:
            dy=d[1]+y
            dx=d[0]+x
            tmp+=parkingLot[dy][dx]
        if '#' in tmp:
                break
        if tmp.count('.') == 4:
            site0 += 1
        elif tmp.count('.') == 3 :
            site1 += 1
        elif tmp.count('.') == 2:
            site2 += 1
        elif tmp.count('.') == 1:
            site3 += 1
        elif tmp.count('.') == 0:
            site4 += 1
print(site0,site1,site2,site3,site4,sep='\n')