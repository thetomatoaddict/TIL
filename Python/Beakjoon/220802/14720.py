# 딸기0 초코1 바나나2
n = int(input())
store = list(map(int, input().split()))
count = 0

for i in range(n):
    if(store[i] == count % 3):
        count+=1

print(count)