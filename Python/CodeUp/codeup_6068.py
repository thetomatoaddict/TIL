#점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.
# 90 ~ 100 : A
# 70 ~  89 : B
# 40 ~  69 : C
# 0 ~   39 : D

n=int(input())

if 89<n<101:
    print('A')
elif 69<n<90:
    print('B')
elif 39<n<70:
    print('C')
elif n<40:
    print('D')