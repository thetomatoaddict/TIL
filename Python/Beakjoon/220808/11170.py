tc=int(input())
for _ in range(tc):
    n,m=map(int, input().split())
    result=str(n).count('0')
    while n != m :
        n+=1
        result+=str(n).count('0')
    print(result)