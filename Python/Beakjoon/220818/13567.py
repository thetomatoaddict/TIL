import sys
sys.stdin = open("13567.txt")
m,n=map(int, input().split())
if m+n == 0:
    print(-1)
    exit()
comm=[]
turn=0
delta=[[1,0],[0,-1],[-1,0],[0,1]]#ESWN
robot=[0,0]
for _ in range(n):
    comm=list(map(str, input().split()))
    if comm[0] == 'MOVE':
        for _ in range(int(comm[1])):
            robot[0]+=delta[turn][0]
            robot[1]+=delta[turn][1]
            if 0>robot[0] or 0>robot[1] or m<robot[0] or m<robot[1]:
                print(-1)
                exit()
                
                  
    elif comm[0] == 'TURN':
        if comm[1] == '0':
            turn-=1
        elif comm[1] == '1':
            turn+=1
        if turn == 4 or turn == -4:
            turn=0
        
print(*robot)
