# 1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.
tc=int(input())

for i in range(tc) :
    n=int(input())
    result=0
    for j in range(1,n+1) :
        if j%2 == 0 :
            result -= j
        else :
            result += j
    print(f'#{i+1} {result}')
