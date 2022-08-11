import sys
input=sys.stdin.readline
n,m=map(int, input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    x,y=map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
visit=[False for _ in range(n+1)]
def dfs(start):
    visit[start]=True
    for i in graph[start]:
        if visit[i]==False:
            dfs(i)
cnt=0
for i in range(1,n+1):
    if visit[i] == False :
        dfs(i)
        cnt += 1

print(cnt)