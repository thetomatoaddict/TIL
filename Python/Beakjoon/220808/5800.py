tc=int(input())
for i in range(tc):
    
    n=list(map(int, input().split()))
    n.pop(0)
    n.sort()
    lg=0
    for j in range(len(n)-1):
        if n[j+1] - n[j] > lg :
            lg = n[j+1] - n[j]
    print(f'Class {i+1}')
    print(f'Max {max(n)}, Min {min(n)}, Largest gap {lg}')

