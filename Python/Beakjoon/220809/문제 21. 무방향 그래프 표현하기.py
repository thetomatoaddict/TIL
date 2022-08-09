from pprint import pprint
n,m=map(int, input().split())
nums=[list(map(int, input().split())) for _ in range(m)]
graph=[[0]*(n+1) for _ in range(n+1)]
list_=[[],[],[],[],[],[],[]]
for i in nums:
    u=i[0]
    v=i[1]
    graph[u][v]=1
    graph[v][u]=1
for i in range(n+1):
    for j in range(n+1):
        if graph[i][j] == 1 :
            list_[i].append(j)

pprint(graph)
print(list_)