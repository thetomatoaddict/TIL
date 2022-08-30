matrix=[]
for i in range(tc):
    for _ in range(5):
        tmp=input()
        tmp+='*'*(15-len(tmp))
        matrix.append(tmp)
    print(f'#{i+1}',end=' ')
    for j in range(15):
        for k in range(5):
            if matrix[k][j] != '*':
                print(matrix[k][j],end='')
    print('\n',end='')
    matrix=[]