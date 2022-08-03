import sys
input = sys.stdin.readline
daydream_cases = int(input())
aPrize=[0,500,300,300,200,200,200,50,50,50,50,30,30,30,30,30,10,10,10,10,10]
bPrize=[0,512,256,256,128,128,128,128,64,64,64,64,64,64,64,64,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32]
for _ in range(daydream_cases):
    a,b=map(int, input().split())
    if a > 21 :
        a=0
    if b > 31 :
        b=0
    print((aPrize[a]+bPrize[b])*10000)