import sys
input = sys.stdin.readline
tc=int(input())
for _ in range(tc):
    n,m=map(int, input().split())
    grid=[list(map(int, input().split())) for _ in range(n)]
    tr_grid = [[0] * n for _ in range(m)]
    for i in range(m):
        flag=0
        for j in range(n):
            if flag == 0 and grid[j][i] == 0 :
                tr_grid[i][j] = '-'
            elif grid[j][i] == 1 :
                flag = 1
                tr_grid[i][j] = grid[j][i]
    cnt=0
    for i in range(m):
        for j in range(n):
            if tr_grid[i][j] == 1 :
                for k in range(j+1,n):
                    if tr_grid[i][k] == 0 :
                        cnt += 1
    print(cnt)
