h,m = map(int,input().split()) 
timer = int(input()) 

if (timer+m)>=60:     # 분 합계 검사
	h_timer=timer//60 
	m_timer=timer%60 
	if (m_timer+m)>59:    # 분 계산
		h=h+((m_timer+m)//60) 
		h=h+h_timer
		m=(m_timer+m)%60 
		if h>24:                   #시 계산
			h=h%24
			print(h,m)
		elif h<24:
			print(h,m)
		elif h==24:
			h=0
			print(h,m)
	elif (m_timer+m)<60:      #분 계산
		h=h+h_timer
		m=m+m_timer
		if h>24:                       #시 계산
			h=h%24
			print(h,m)
		elif h<24:
			print(h,m)
		elif h==24:
			h=0
			print(h,m)
elif (timer+m)<60:          # 분 합계검사, 분 계산
	m=m+timer
	print(h,m)
