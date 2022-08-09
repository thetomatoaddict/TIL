n = int(input())
answerBoard = [list(input()) for _ in range(n)]
checkBoard = [list(input()) for _ in range(n)]
result = []
bomb = False

# 지뢰를 둘러싼 좌표셋(x,y)
dx = [1,0,-1,0,1,-1,1,-1]
dy = [0,1,0,-1,-1,1,1,-1]

for i in range(n):
    temp = []
    for j in range(n):
        cnt = 0
        if checkBoard[i][j] == 'x' and answerBoard[i][j] == '*':
            bomb = True
        if checkBoard[i][j] == 'x':
            for k in range(8):
                if n>(i+dx[k])>=0 and n>(j+dy[k])>=0 and answerBoard[i + dx[k]][j + dy[k]] == '*':
                    cnt += 1
            temp.append(str(cnt))
        else:
            temp.append('.')
    result.append(temp)

if bomb:
   for i in range(n):
        for j in range(n):
            if answerBoard[i][j] == '*':
                result[i][j] = '*'

for data in result:
    print(''.join(data))