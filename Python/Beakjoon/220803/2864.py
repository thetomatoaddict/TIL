nums=input().split()

#최소값
a=int(nums[0].replace('6', '5'))
b=int(nums[1].replace('6', '5'))
print(a+b,end=' ')

#최대값
a=int(nums[0].replace('5', '6'))
b=int(nums[1].replace('5', '6'))
print(a+b)