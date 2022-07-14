# rgb 빛들을 섞어 만들 수 있는 모든 경우의 조합(r g b)과
# 만들 수 있는 색의 가짓 수를 계산해보자.  

r,g,b=map(int, input().split()) # 2 2 2 

for i in range(0,r): # 0 
    for j in range(0,g): # 0 / 1
        for k in range(0,b): #0 1 2 /
            print(i,j,k) # 0 0 0 / 0 0 1 / 0 0 2 /
print(r*g*b)