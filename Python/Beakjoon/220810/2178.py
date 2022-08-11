n,m=map(int, input().split())

road=[list(input()) for _ in range(n)]
visit=[[False]*m for _ in range(n)]
delta=[[1,0],[-1,0],[0,1],[0,-1]]
result=[]
cnt=0
def dfs(y,x):
    if y==n-1 and x==m-1:
        result.append(cnt)

    for d in delta:
        dy=d[0]+y
        dx=d[1]+x
        if 0<=dy<n and 0<=dx<m :
            if road[dy][dx] == 1 and visit[dy][dx] == False:
                visit[dy][dx] = True
                cnt+=1
                dfs(dy, dx)
dfs(0, 0)
print(result)