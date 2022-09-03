from collections import Counter
n=int(input())
name=[]
for _ in range(n):
    name.append(list(input().split('.'))[1])

name=Counter(name)
name=sorted(name.items(), key=lambda x: x[0])

for i,j in name :
    print(i,j)