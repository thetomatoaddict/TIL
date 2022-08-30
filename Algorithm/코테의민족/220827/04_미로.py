delta=[[0,1],[1,0],[-1,0],[0,-1]]
result=0
def dfs(y,x):
    global result
    visit[y][x] = True
    for dy,dx in delta:
        ny=y+dy
        nx=x+dx
        if 0<=ny<16 and 0<=nx<16:
            if maze[ny][nx] == 0 and visit[ny][nx] == False:
                dfs(ny, nx)
            elif maze[ny][nx] == 3 :
                result = 1
                return result


for tc in range(1,11):
    input()
    maze=[list(map(int, input())) for _ in range(16)]
    visit=[[False]*16 for _ in range(16)]
    dfs(1,1)
    print(f'#{tc} {result}')
    result=0