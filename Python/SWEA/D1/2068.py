#10개의 수를 입력 받아,
#그 중에서 가장 큰 수를 출력하는 프로그램을 작성하라.

testCase=int(input())

for nthTest in range(1,testCase+1):
    nums=list(map(int, input().split()))
    print(f'#{nthTest}',max(nums))