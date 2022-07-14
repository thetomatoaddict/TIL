# 알파벳 대소문자로 된 단어가 주어지면,
# 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
# 단, 대문자와 소문자를 구분하지 않는다.

a=input()
a_list=sorted(a.upper())#알파벳순으로 정렬하여 대문자 리스트로 저장
max_c=1
result=str()
for i in range(65,91): #대문자 아스키코드로 알파벳 26개마다 일치하는 갯수 검사
    if max_c < a_list.count(chr(i)):
        max_c=a_list.count(chr(i))
        result=str()
        result=chr(i)
        a_list.remove(chr(i))

for i in range(65,91):
    if max_c == a_list.count(chr(i)):
        max_c=a_list.count(chr(i))
        result += chr(i)

if len(result)==1:
    print(result)
else :
    print('?')

print(result)
