a=int(input())
b=list(map(int, input().split()))
new=int(0)
for i in range(a):
    n=b[i]/max(b)*100
    new=new+n
print(new/a)