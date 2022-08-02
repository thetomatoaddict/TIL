import sys
input = sys.stdin.readline
n=int(input())
names={}
for _ in range(n):
    name=input()
    names[name[0:-6]]=name[-5]
names=sorted(names.items(),reverse=True)
for k,v in names:
    if v == 'e':
        print(k)