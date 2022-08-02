from collections import Counter
import sys
input = sys.stdin.readline

n=int(input())
names=[]
for _ in range((n*2)-1):
    names.append(input())

names=Counter(names)

for i in sorted(names.items(),key=lambda x:x[1]):
    if int(i[1])%2 != 0 :
        print(i[0])
        break