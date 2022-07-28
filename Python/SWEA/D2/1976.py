tc=int(input())
for i in range(tc):
    A,a,B,b=map(int, input().split())
    a+=b
    if a > 59 :
        A+=1
    A+=B
    if A > 12 :
        A-=12
    print(f'#{i+1} {A} {a}')