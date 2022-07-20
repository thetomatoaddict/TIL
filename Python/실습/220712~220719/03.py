n=int(input())
r=0

for i in range(n+1):
    r+=i

while n!=0:
    r+=n
    n-=1

print(r)