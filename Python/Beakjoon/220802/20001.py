input()
stack=[]
line=''
while line != '고무오리 디버깅 끝' :
    line=input()
    if line == '문제':
        stack.append('문제')
    elif line == '고무오리':
        if len(stack) > 0 :
            stack.pop()
        elif len(stack) == 0 :
            stack.append('문제')
            stack.append('문제')

if len(stack) > 0 :
    print('힝구')
elif len(stack) == 0 :
    print('고무오리야 사랑해')

