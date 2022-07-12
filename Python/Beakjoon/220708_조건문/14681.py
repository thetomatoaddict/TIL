x=int(input())
y=int(input())

if x>0:
	if y>0:
		print('1')
	elif y<0:
		print('4')
elif x<0:
	if y<0:
		print('3')
	elif y>0:
		print('2')
