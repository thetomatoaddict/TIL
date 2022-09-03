word=['m', 'i', 'r', 'k', 'o', 'v', 'C', '4']
bomb='C4'
stack=[]
for i in word:
    stack.append(i)
    if ''.join(stack[-2:]) == bomb :
        for _ in range(2):
            stack.pop()

print(stack)