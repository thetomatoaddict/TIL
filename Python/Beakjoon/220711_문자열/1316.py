a  = int(input())                  # a를 입력받는다(반복할 횟수)

for i in range(a):                 # a만큼 반복한다
    lst = []                       # 리스트 생성
    b = input()                    # b를 입력받는다(체크할 문자)
    while len(b) != 0:             # 입력받은 문자의 길이가 0이 아니면 반복한다
        lst.append(b[0])           # 문자열의 첫번째 문자를 리스트에 추가
        b = b.lstrip(b[0])         # 리스트에 추가한 문자를 지운다(같은문자가 연속해서있으면 같이 지움)

    for i in lst:                  # 리스트에 저장된 문자
       if lst.count(i) > 1:        # 저장된 문자의 개수가 1개 이상이면
            a -= 1                 # a에서 1 차감(그룹단어가 아닌개수 차감)
            break

print(a)                           # a를 프린트한다