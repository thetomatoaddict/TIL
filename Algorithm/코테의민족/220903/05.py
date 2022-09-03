word=input().rstrip('\n')
stack=[]
for i in word:
    stack.append(i)
    if ''.join(stack[-4:]) == 'PPAP' :
        del stack[-4:]
        stack.append('P')

if len(stack) == 1 and stack[0]=='P':
    print('PPAP')
else :
    print('NP')