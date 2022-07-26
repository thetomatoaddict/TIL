a,b=map(int, input().split())

if (a-b)%2 == 0 : # 작은 수가 이겨요
    print('B' if a > b else 'A')
elif (a-b)%2 != 0 : # 큰 수가 이겨요
    print('A' if a > b else 'B') 