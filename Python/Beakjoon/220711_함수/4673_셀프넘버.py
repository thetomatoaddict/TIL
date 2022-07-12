numbers=set(range(1,20))
nonself=set()
for i in numbers: # 예를 들어 i가 12일 경우
    for j in str(i): # 12를 문자열로 변환하여 1, 2로 접근 
        i += int(j) # d(i) = i+j1+j2 = 12+1+2 = 24
    nonself.add(i) # 생성자가 있는 논셀프넘버(예:24)를 집합으로 모은다
self_num = numbers - nonself # 전체 숫자집합에서 논셀프넘버 집합을 뺀다
for k in sorted(self_num): #셀프넘버 집합을 오름차순으로 정렬
    print(k) #작은 수부터 하나씩 각 줄에 출력