s=str(input())
n=[]
for i in range(len(s)): # 한 글자씩 검사
    for j in range(97,123): # 글자를 26번 검사
        if chr(j) == s[i] : # 아스키코드 찾으면 기록
            n.append(i)
            break
        else :
            n.append(-1) #아스키코드 없으면 -1기록
    

print(n,sep=" ")


