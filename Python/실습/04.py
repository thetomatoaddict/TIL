n=int(input())
r=1

for i in range(n):
    r*=i+1

while n!=0:
    r*=n
    n-=1

print(r)
