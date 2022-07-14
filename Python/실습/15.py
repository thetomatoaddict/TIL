a=input()
b=0
for i in range(len(a)):
    if a[i] == 'a':
        print(i)
        b=1
        break
if b==0:
    print('-1')

#추가문제

a=input()

for i in range(len(a)):
    if a[i] == 'a':
        print(i,end=' ')
