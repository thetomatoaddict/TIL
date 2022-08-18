import sys
sys.stdin = open("1926.txt")
sys.setrecursionlimit(100000)

n,m=map(int, input().split())

imap=[list(map(int, input().split())) for _ in range(n)]
delta=[[-1,0],[0,-1],[0,1],[1,0]]
area=0
result=0
def dfs(y,x):
    global area
    area+=1
    imap[y][x]=0
    for d in delta:
        ny=y+d[0]
        nx=x+d[1]
        if 0<=ny<n and 0<=nx<m:
            if imap[ny][nx] == 1 :
                dfs(ny, nx)
cnt=0
for i in range(n):
    for j in range(m):
        if imap[i][j] == 1:
            dfs(i, j)
            cnt+=1
            if area > result:
                result=area
            area=0
            
print(cnt)
print(result)