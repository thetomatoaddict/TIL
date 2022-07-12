#입력된 세 정수 a, b, c 중 가장 작은 값을 출력

a, b, c = map(int,input().split()) #1,2,3이라면
print((a if a<b else b) if ((a if a<b else b)<c) else c)
# a if a<c else c
# 가장 안쪽 괄호에서 a와 b를 비교하고,
# 바깥쪽에서는 안쪽 결과와 C를 비교한다.