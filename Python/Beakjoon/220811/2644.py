import sys
sys.stdin = open("2644.txt")
sys.setrecursionlimit(10000) #재귀함수 제한을 늘려줌
n=int(input())
a,b=map(int, input().split())
m=int(input())

graph=[[] for _ in range(n+1)]
visit=[False for _ in range(n+1)]
cnt=[0 for _ in range(n+1)]
for _ in range(m):
    x,y=map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(start):
    visit[start]=True
    if start == b:
        print(cnt[start])
        exit()
    for i in graph[start]:
        if visit[i] == False:
            cnt[i]+=cnt[start]+1
            dfs(i)
dfs(a)
print(-1)