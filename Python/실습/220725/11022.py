tc=int(input())

for testcase in range(tc):
    a,b=map(int, input().split())
    print(f'Case #{testcase+1}: {a} + {b} = {a+b}')