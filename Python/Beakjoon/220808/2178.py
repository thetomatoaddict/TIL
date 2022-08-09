n,m = map(int,input().split())


maze=[]
pos_queue = [(0,0)] # 내가 움직인 포지션을 기록
cnt_queue = [1] # 내가 움직인 칸수

wall,check = 0,0 # 못가는길,방문처리
road = 1 # 갈수있는 길

end_pos = (n-1,m-1)
for i in range(n):
    mc = list(map(int,list(input())))
    maze.append(mc)

# 좌표값을 입력받아 갈수 있는길인지 확인
def is_can_go(x,y):
    if(0<=x<n and 0<=y<m):
        if (maze[x][y] == road):
            return True
        else:
            return False
    return False
# 큐가 비어있을때까지 반복함
while len(pos_queue)!=0:
    # 앞에있는 값을 꺼냄
    pos = pos_queue.pop(0)
    cnt = cnt_queue.pop(0)
    # 튜플형태를 x,y로 지정
    x = pos[0]
    y = pos[1]
    if (pos == end_pos): # 현재 위치가 도착지점일때 cnt 출력하고 break
        print(cnt)
        break
    elif (maze[x][y] == wall): # 현재 위치가 벽일경우 continue 
        continue
    maze[x][y] = check  # 방문처리 => 한번 갔던길은 다시 체크할 필요 없기때문에
                        # 이미 방문한 길은 continue로 계산을 건너뜀
    if(is_can_go(x+1,y)):  # 상하좌우로 갈수 있는지 확인하고 갈수 있으면 큐에 담음
        pos_queue.append((x+1,y))# 좌표를 담을 큐
        cnt_queue.append(cnt+1)# 칸수를 담을 큐
    if(is_can_go(x-1,y)):
        pos_queue.append((x-1,y))
        cnt_queue.append(cnt+1)
    if(is_can_go(x,y-1)):
        pos_queue.append((x,y-1))
        cnt_queue.append(cnt+1)
    if(is_can_go(x,y+1)):
        pos_queue.append((x,y+1))
        cnt_queue.append(cnt+1)
   