n,m=map(int, input().split())
card=list(map(int, input().split()))
result=[]
for i in range(n):
    for j in range(i+1,n):
        for k in range(i+2,n):
            if card[i] != card[j] and card[j] != card[k] and card[i] != card[k] :
                if card[i]+card[j]+card[k] > m :
                    continue
                else :
                    result.append(card[i]+card[j]+card[k])
print(max(result))