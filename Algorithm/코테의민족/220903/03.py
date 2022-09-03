from collections import deque
n=int(input())
drivein=[]
driveout=deque()
cnt=0
for _ in range(n):
    drivein.append(input())

for _ in range(n):
    driveout.append(input())

while driveout :
    if drivein[0] != driveout[0] :
        drivein.pop(drivein.index(driveout.popleft()))
        cnt+=1

    else:
        drivein.pop(0)
        driveout.popleft()

print(cnt)
        
