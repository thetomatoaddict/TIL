import sys
from collections import deque
sys.stdin = open("./1926.txt")
input = sys.stdin.readline

n,m=map(int, input().split())
map_=[list(map(int, input().split())) for _ in range(n)]
visit=[[False] * m for _ in range(n)]

dy=[0,1,0,-1]
dx=[1,0,-1,0]

def bfs(y,x):
    area=1
    q=deque()
    q.append((y,x))
    while q:
        ey, ex =q.popleft()
        for d in range(4):
            ny = ey + dy[d]
            nx = ex + dx[d]
            if 0<=ny<n and 0<=nx<m :
                if map_[ny][nx]==1 and visit[ny][nx] == False:
                    area+=1
                    visit[ny][nx] = True
                    q.append((ny,nx))
    return area



cnt=0
result=0
for i in range(n):
    for j in range(m):
        if map_[i][j] == 1 and visit[i][j]==False:
            visit[i][j] = True
            cnt+=1
            result = max(result, bfs(i, j))            
print(cnt)
print(result)