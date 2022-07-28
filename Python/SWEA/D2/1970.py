tc=int(input())
cash=[50000,10000,5000,1000,500,100,50,10]
for i in range(tc):
    change=int(input())
    print(f'#{i+1}')
    for j in cash:
        if j == 10:
            print(change//j,end='\n')
        else : 
            print(change//j,end=' ')
            change%=j