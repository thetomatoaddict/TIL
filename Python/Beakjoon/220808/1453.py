from collections import Counter
n=int(input())
nl=Counter(list(map(int, input().split())))
cnt=0
for k,v in nl.items():
    if v > 1 :
        cnt += v-1
print(cnt)