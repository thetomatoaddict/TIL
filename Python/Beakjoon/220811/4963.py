import sys
sys.stdin = open("4963.txt")
sys.setrecursionlimit(10000)
while True:
    w,h=map(int, input().split())
    if w+h == 0 :
        break
    imap=[list(map(int, input().split())) for _ in range(h)]
    delta=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        
    def dfs(y,x):
        imap[y][x]=0
        for d in delta:
            ny=y+d[0]
            nx=x+d[1]
            if 0<=ny<h and 0<=nx<w:
                if imap[ny][nx] == 1 :
                    dfs(ny, nx)
    cnt=0
    for i in range(h):
        for j in range(w):
            if imap[i][j] == 1:
                dfs(i, j)
                cnt+=1
    print(cnt)