tc=int(input())
for _ in range(tc):
    price=int(input())
    ops=int(input())
    for _ in range(ops):
        n,m=map(int, input().split())
        price+=n*m
    print(price)