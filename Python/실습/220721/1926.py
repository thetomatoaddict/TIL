# 입력으로 정수 N 이 주어졌을 때, 1~N 까지의 숫자를

# 게임 규칙에 맞게 출력하는 프로그램을 작성하라.

n=int(input())
clap=0
for i in range(1,n+1):
    clap=0
    for j in str(i):
        if j in '369':
            print('-',end='')
            clap+=1
    if clap == 0 :
        print(i,end='')
    print(' ',end='')
        