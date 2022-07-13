a=input()
b=list(a)
c=0
result=str()

for i in range(len(b)):
    c-=1
    result += b[c]

print(result)