tc=int(input())
for i in range(tc):
    n=int(input())
    nums=list(map(int, input().split()))
    nums.sort()
    print(f'#{i+1}',*nums)