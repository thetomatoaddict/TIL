dy=[0, 1, -1, 1]
dx=[1, 0, 1, 1]
black=1
white=2
n=19
board=[]


for y in range(n):
    for x in range(n):
        for d in range(4):
            if board[y][x] == 1 or board[y][x] == 1 :
                ny=y+dy[d]
                nx=x+dx[d]

                while True:
                    if not(-1 < ny < n and -1 < nx < n):
                        break
                    if not(board[y][x] == boardp[ny][nx]):
                        break
                    stone_cnt+=1
                    ny += dy[d]
                    nx += dx[d]
                    if stone_cnt == 5 :
                        prev_y = y - dy[d]
                        prev_x = x - dx[d]
