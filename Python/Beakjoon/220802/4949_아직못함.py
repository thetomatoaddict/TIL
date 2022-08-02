# import sys
# input = sys.stdin.readline

# while True :
#     line=input().rstrip()
#     if line == '.' :
#         break
#     if line == ' .' :
#         print('yes')
#         break
    
#     brackets=''
#     Lresult=0
#     Sresult=0
#     for letter in line:
#         if letter in '[]()':
#             brackets+=letter
            
#     for bracket in brackets:
#         if '(]' in brackets or '[)' in brackets:
#             Lresult=1
#             break
#         if brackets[-1] == ']' :
#             Lresult=1
#             break
#         if Lresult < 0 or Sresult < 0:
#             break
#         elif bracket == '[' :
#             Lresult+=1
#         elif bracket == '(' :
#             Sresult+=1
#         elif bracket == ']' :
#             Lresult-=1
#         elif bracket == ')' :
#             Sresult-=1
        

#     print("yes" if Sresult == 0 and Lresult == 0 else "no")

import sys
input = sys.stdin.readline

while(True):
    string = input()
    if string == '.\n':
        break

    i = 0
    stack = []
    check = True
    while(i < len(string) - 1):
        if string[i] == '(' or string[i] == '[': #열린 괄호 push 하기
            stack.append(string[i])
        elif string[i] == ')' or string[i] == ']': #닫힌 괄호면 pop하고 맞는지 검사하기
            if stack:
                pop = stack.pop()
                if (pop == '(' and string[i] == ')') or (pop == '[' and string[i] == ']'):
                    # 리스트에서 pop된 괄호가 현재 닫힘괄호와 같은 종류의 열림괄호인지 검사
                    check = True 
                else:
                    check = False
                    break
            else:
                check = False
                break
        i += 1
    if stack:
        check = False
    print('yes') if check else print('no')