n=int(input())
m=int(input())
prime=list(range(n,m+1))

for i in range(n,m+1):
    for j in range(2,i) :
        if i % j == 0 :
            prime.remove(i)
            break
if 1 in prime:
    prime.remove(1)
print(f'{sum(prime)}\n{min(prime)}' if len(prime) > 0 else -1)