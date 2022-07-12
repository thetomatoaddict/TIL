case=int(input())
temp=str()

for i in range(case): # 2번 반복
    a,b=input().split() # a,b를 str으로 입력받음
    for j in range(len(b)): # b의 문자갯수만큼 반복
        temp+=(b[j]*int(a)) #temp에 b의 문자열을 a번 반복시켜 저장
    print(temp)
    temp=str()