from collections import Counter
 
T = int(input())
 
for test_case in range(1, T + 1):
    num=int(input())
    counter = Counter(list(map(int, input().split())))
    print("#%d" %test_case, counter.most_common(n=1)[0][0])