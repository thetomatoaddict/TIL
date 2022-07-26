#입력으로 N 개의 점수가 주어졌을 때, 중간값을 출력하라.

T = int(input())
numbers = list(map(int,input().split()))
numbers.sort()
 
print(numbers[T//2])