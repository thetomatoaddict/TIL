# 날짜가 유효하다면

# [그림1] 과 같이 ”YYYY/MM/DD”형식으로 출력하고,

# 날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.

tc = int(input())
for i in range(tc):
    date_l=[]
    date=input()
    date_l.append(date[0:4])
    date_l.append(date[4:6])
    date_l.append(date[6:8])
    if int(date_l[1]) > 12 or int(date_l[1]) == 0 or int(date_l[2]) == 0:
        print(f'#{i+1} -1')
    elif date_l[1] in '01,03,05,07,08,10,12' and int(date_l[2]) > 31 :
        print(f'#{i+1} -1')
    elif date_l[1] in '09,11,04,06' and int(date_l[2]) > 30 :
        print(f'#{i+1} -1')
    elif date_l[1] == '02' and int(date_l[2]) > 28 :
        print(f'#{i+1} -1')
    else :
        print(f'#{i+1} {date_l[0]}/{date_l[1]}/{date_l[2]}')
             
