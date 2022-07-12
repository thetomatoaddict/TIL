n1=int(input())
h_count=0
for i in range(1,n1+1): #예를 들어 i=123이다
    num=list(map(int, str(i)))
    if i < 100 :
        h_count+=1
    elif num[0]-num[1] == num[1]-num[2] :
        h_count+=1

print(h_count)