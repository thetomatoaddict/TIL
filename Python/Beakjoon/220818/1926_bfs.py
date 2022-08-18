from collections import deque
n, m = map(int, input().split(' '))
g = []

for i in range(n) :
  g.append(list(map(int, input().split(' '))))

visited = [[False] * m for _ in range(n)]
cntArr = []

def bfs(x, y) :
    q = deque()
    cnt = 0
    q.append((x, y))
    visited[x][y] = True

    move = [[0, -1], [0, 1], [-1, 0], [1, 0]]

    while q :
        x, y = q.popleft()
        cnt += 1

        for i in range(4) :
            nx, ny = move[i][0] + x, move[i][1] + y

            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue

            if g[nx][ny] == 1 and not visited[nx][ny] :
                q.append((nx, ny))
                visited[nx][ny] = True

    cntArr.append(cnt)
    return True


res = 0
for i in range(n) :
    for j in range(m) :
        if g[i][j] == 1 :
            if not visited[i][j] and bfs(i, j):
                res += 1

print(res)

if res == 0 :
    print(0)
else :
    print(max(cntArr))

