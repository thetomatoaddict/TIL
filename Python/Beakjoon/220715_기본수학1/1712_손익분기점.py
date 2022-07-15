a,b,c=map(int,input().split())
#a=고정지출 b=노트북1대당생산비 c=노트북1대가격
print('-1' if b>c else a//(c-b)+1)

