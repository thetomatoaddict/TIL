# 민석이는 1번 양부터 순서대로 세는 것이 재미없을 것 같아서 N의 배수 번호인 양을 세기로 하였다.
tc=int(input())

for i in range(tc):
    n=int(input())
    nums=set()
    cnt=0
    while len(nums) != 10 :
        cnt += 1
        n*=cnt
        for j in str(n):
            nums.add(j)
    print(n,nums)




