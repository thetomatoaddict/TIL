n=int(input())
temp=0
for i in range(n+1):
    temp+=i
    if temp>=n:
        print(temp)
        break