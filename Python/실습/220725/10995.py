n=int(input())

for i in range(n):   #5
    if i%2 != 0 :
        print(' ',end='')
    for j in range(n):
        print('*',end=' ')
    print('')