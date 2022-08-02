tc=int(input())

for _ in range(tc):
    input()
    n=set(input().split())
    input()
    m=input().split()
    for i in m:
        if i in n:
            print(1)
        else :
            print(0)
        