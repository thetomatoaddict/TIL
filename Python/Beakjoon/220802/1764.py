import sys
# input = sys.stdin.readline

n,m=map(int, input().split())
dj = [sys.stdin.readline() for _ in range(n)]
bj = [sys.stdin.readline() for _ in range(m)]

result=sorted(list(set(dj)&set(bj)))
print(len(result))
for i in result:
    print(i.rstrip())
