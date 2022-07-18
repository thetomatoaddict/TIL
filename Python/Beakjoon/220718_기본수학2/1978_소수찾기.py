n=int(input())
nums=list(map(int, input().split()))

for i in nums:
    if i == 1 :
        n -= 1
    for j in range(2,i):
        if i%j == 0 :
            n -= 1
            break
print(n)
