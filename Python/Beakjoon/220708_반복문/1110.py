n=int(input())
new=n
cy=0
while True :
    a=new//10 #수의 앞자리
    b=new%10 # 수의 뒷자리
    c=(a+b)%10 # 앞뒤 합의 뒷자리
    new=10*b+c
    cy=cy+1
    if (n==new):
        break

print(cy)




    
    