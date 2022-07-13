a=input()
b=list(a)
result=str()

for i in range(len(b)):
    if b[i] != ('a'):
        result+=b[i]

print(result)