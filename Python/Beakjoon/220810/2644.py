from collections import deque

n=int(input())
a,b=map(int, input().split())
m=int(input())

board = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m) :
    x,y=map(int, input().split())
    board[x].append(y)
    board[y].append(x)

def bfs(s): #7
    queue=deque([s]) #7 #2
    visited[s]=1 # visited[7] = 1 #visited[2] =1
    while queue: #queue 가 True일 동안
        x=queue.popleft() # x=7 # x=2
        for nx in board[x]: #board[7]=2 #board[2]=1,7,8,9
            if nx == b : 
                print(visited[x])
                print(board)
                print(visited)
                exit()
            if not visited[nx]: # visited[2]가 0이 아니면 
                visited[nx] = visited[x]+1 #visited[2]=1 #visited[1]=1
                queue.append(nx) #큐에 2를 더함

bfs(a)
print(-1)