# https://www.acmicpc.net/problem/9935

word=input().rstrip('\n')
bomb=input().lstrip(' ')
n=len(bomb)
stack=[]
for i in word:
    stack.append(i)
    if ''.join(stack[-n:]) == bomb :
        for _ in range(n):
            stack.pop()


if len(stack) == 0:
    print('FRULA')
else :
    print(*stack,sep='')



