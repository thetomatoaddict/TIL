#입력으로 N 개의 점수가 주어졌을 때, 중간값을 출력하라.

n=int(input())
nums=list(map(int, input().split()))
nums.sort()
# n=round(n/2)+1
# print(nums[-n])
print(nums)