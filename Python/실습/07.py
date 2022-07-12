
ns=list(map(int, input().split()))
ns.sort()
print(ns[0])

#sort메서드,len함수 없이 만들기

ns=list(map(int, input().split()))
min_n=0
for i in ns:
    if min_n > i:
        min_n=i

print(min_n)
