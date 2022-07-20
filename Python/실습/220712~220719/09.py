students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']

#메서드 사용하는 경우
print(students.count('이영희'))

#반복문으로 세는 경우
c=0
for i in students:
    if i == '이영희':
        c+=1
print(c)