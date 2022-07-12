n=int(input())
scr=int(0)
result=int(0)
for i in range(n):
    a=list(input())
    for j in range(len(a)):
        if a[j] == 'O':
            scr=scr+1
            result=result+scr
        elif a[j] == 'X':
            scr=0
    print(result)
    scr=0
    result=0
