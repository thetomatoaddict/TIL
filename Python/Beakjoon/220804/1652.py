import sys
input = sys.stdin.readline
def sleep_site(room):
    avilable_line=0
    for i in room:
        cnt=0
        for j in range(len(i)):
            if i[j] == '.':
                cnt+=1
                if j == len(i)-1:
                    if cnt >= 2:
                        avilable_line+=1
            elif i[j] == 'X':
                if cnt >= 2:
                    avilable_line+=1
                cnt=0            
    return avilable_line



n=int(input())

vanila_room=[input().rstrip() for _ in range(n)] # 기본 배열

transposed_room = [[0] * n for _ in range(n)] #행,열을 맞바꾼 배열
for i in range(n):
  for j in range(n):
    transposed_room[i][j] = vanila_room[j][i]

print(sleep_site(vanila_room), sleep_site(transposed_room))





