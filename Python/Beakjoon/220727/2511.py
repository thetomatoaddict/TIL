A=list(map(int, input().split()))
B=list(map(int, input().split()))
a=0
b=0
lastround=0
for i in range(10):
    if A[i] > B[i]:
        a+=3
        lastround=i
    if A[i] < B[i]:
        b+=3
        lastround=i
    if A[i] == B[i]:
        a+=1
        b+=1
print(a,b)


if a==b and A[lastround]!=B[lastround]:
    print('A' if A[lastround]>B[lastround] else 'B')
elif a==b and A[lastround]==B[lastround]:
    print('D')
else : print('A' if a>b else 'B')
