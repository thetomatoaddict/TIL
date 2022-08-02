import sys
from collections import Counter
input = sys.stdin.readline

n=int(input())
nums = [int(input().rstrip()) for _ in range(n)]
nums = Counter(nums).most_common()
result= [k for k,v in nums if nums[0][1] == v]
print(min(result))