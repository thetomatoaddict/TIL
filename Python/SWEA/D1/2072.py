# 10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.
testCase=int(input())

for nthTest in range(1,testCase+1):
    nums=list(map(int, input().split()))
    for i in range(10):
        if nums[i]%2 == 0 :
            nums[i]=0
    print(f'#{nthTest}',sum(nums))