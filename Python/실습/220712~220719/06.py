#최대값
ns=list(map(int, input().split()))
ns.sort()
print(ns[-1])

#sort메서드,len함수 없이 만들기

ns=list(map(int, input().split()))
max_n=0
for i in ns:
    if max_n < i:
        max_n=i

print(max_n)
