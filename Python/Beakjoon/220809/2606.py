n=int(input())
m=int(input())

graph=[[] for _ in range(n+1)]

for i in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visit=[0]*(n+1)

def dfs(graph, v, visited):
    visit[v] = 1 
    for i in graph[v]: 
        if visit[i] == 0 : 
            dfs(graph, i, visited)

dfs(graph, 1, visit)
print(visit.count(1)-1)
print(graph)