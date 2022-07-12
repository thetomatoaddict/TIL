s=str(input()) #baekjoon
n=str()
find=0

for i in range(97,123): #26번 검사
    for j in range(len(s)): # 한 알파벳 당 8번 비교
        if chr(i) == s[j] : # 아스키코드 찾으면 기록
            n+=str(j)
            n+=" "
            find=1
            break
    if find!=1:
        n+='-1 ' #아스키코드 없으면 -1기록
    find=0

print(n)
