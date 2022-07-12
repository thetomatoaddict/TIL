ns=list(map(int, input().split()))
max_n=0
max_nd=0
for i in ns:
    if max_n < i:
        max_nd=max_n
        max_n=i

print(max_nd)
