n=int(input())
for i in range(n):
    a,b=map(int, input().split())
    print(f'#{i+1}',a//b,a%b)