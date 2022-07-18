#문자열 a가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
a=input()
count=0

for i in a:
	if i in 'aeiou':
		count+=1

print(count)