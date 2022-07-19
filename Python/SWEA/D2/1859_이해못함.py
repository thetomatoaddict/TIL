# #https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LrsUaDxcDFAXc
# 1. 원재는 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
# 2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있다.
# 3. 판매는 얼마든지 할 수 있다.
testCase=int(input())

for nthTest in range(testCase):
    days=int(input())
    price=list(map(int, input().split()))
    maxPrice=price[-1] #price 리스트의 맨 뒤에서 시작
    result=0
    for i in range(days-1, -1, -1): #price 리스트의 맨 뒤에서부터
        if price[i] >= maxPrice :
            maxPrice=price[i]
        else :
            result += maxPrice - price[i]
    print(f'#{nthTest+1}',result)