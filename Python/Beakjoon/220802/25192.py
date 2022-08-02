n=int(input())
result=0
temp=set()
for i in range(n):
    line=input()
    if line != 'ENTER':
        temp.add(line)
    elif line == 'ENTER':
        if len(temp) > 0:
            result += len(temp)
            temp.clear()
        elif len(temp) == 0:
            continue
result += len(temp)
print(result)
