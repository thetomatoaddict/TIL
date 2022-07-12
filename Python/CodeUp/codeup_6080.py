#1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때,
# 나올 수 있는 모든 경우를 출력해보자.

n,m=map(int, input().split())

for i in range(n):
    for j in range(m):
        print(i+1,j+1)
