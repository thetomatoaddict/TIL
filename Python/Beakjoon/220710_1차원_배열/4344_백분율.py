a=int(input())
temp=int()
human=int()
result=int()
for i in range(a):
    b=list(map(int, input().split()))
    for j in range(b[0]): #합계만들기
        temp=temp+b[j+1]
    temp=temp/b[0] #평균내기
    for j in range(b[0]): #평균 이상인 학생 수 세기
        if b[j+1] > temp:
            human=human+1
    result=human/b[0]*100
    print(f'{result:.3f}%')
    temp=0
    human=0
    result=0
