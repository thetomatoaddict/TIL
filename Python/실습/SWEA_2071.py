n=int(input())

for i in range(n):
    nums=list(map(int, input().split()))
    print(f'#{i+1}',f'{sum(nums)/10:.0f}',sep=' ')
