from collections import deque
import sys
input=sys.stdin.readline

n,k=map(int, input().split())
s,rx,ry=map(int, input().split())
virus=[list(map(int, input().split())) for _ in range(n)]


dy=[0,1,0,-1]
dx=[1,0,-1,0]

q=deque()

for i in range(n):
    for j in range(n):
        q.append((i,j))

def bfs():
    rs=[]
    while q:
        y,x=q.popleft()
        for d in range(4):
            ny=y+dy[d]
            nx=x+dx[d]
            if 0<=ny<n and 0<=nx<m :
                if virus[ny][nx] == 0:
                    virus[ny][nx]=virus[y][x]+1
                    q.append((ny,nx))
    for i in range(n):
        rs+=virus[i] 
    return rs
result=bfs()
if result.count(0) > 0 :
    print(-1)
else :
    print(max(result)-1)




    
