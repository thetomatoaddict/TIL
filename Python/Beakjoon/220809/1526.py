n=int(input())
tmp=''
result=[]
for i in range(4,n+1):
    tmp=str(i).replace('4', '').replace('7', '')
    if len(tmp) == 0 :
        result.append(i)
print(max(result))