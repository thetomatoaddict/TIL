from pprint import pprint
delta=[[1,0],[-1,0],[0,1],[0,-1]]
visit = []
map_=[]
cnt=0

def is_island(i,j):
    visit[i][j]=True
    if map_[i][j] == 1 :
        for d in delta:
            dy=i+d[0]
            dx=j+d[1]
            if 0>dy or dy>=h or 0>dx or dx>=w:
                continue
            if visit[dy][dx] == False and map_[dy][dx] == 1:
                is_island(dy,dx)

while True:
    w,h=map(int, input().split())
    if w+h==0:
        break
    map_=[list(map(int, input().split())) for _ in range(h)]
    visit = [[False]*w for _ in range(h)]
    if h>1:
        for i in range(h):
            for j in range(w):
                if visit[i][j]==False and map_[i][j] == 1 :
                    is_island(i, j)
                    cnt+=1
                    

        print(cnt)
        pprint(visit)
    else :
        print(0)