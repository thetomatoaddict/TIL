import sys
sys.setrecursionlimit(10000) #재귀함수 제한을 늘려줌

sys.stdin = open("1_연결 요소의 개수.txt")

def dfs(start):
    # 재귀함수로 만든 dfs
    # 시작 노드와 연결된 모든 노드를 방문
    visited[start] = True
    for i in net[start]:
        if not visited[i]:
            dfs(i)

All_c,connect_c =map(int,sys.stdin.readline().split())
# sys.stdin.readline()를 사용하지 않으면 타임아웃 오류 발생
net = [[] for _ in range(All_c + 1)] # 그래프 생성

visited = [False] * (All_c+1) # False로 초기화

C_cnt = 0

for _ in range(connect_c):
    k,v = map(int,sys.stdin.readline().split())
    net[k].append(v)
    net[v].append(k)
    # 무방향 그래프 이므로 각각의 노드에서 모두 연결됨
    # net[v].append(k)를 제거하면 유방향 그래프가 됨

for i in range(1,All_c+1):
    if not visited[i]: # 만약 방문하지 않은 노드라면
        dfs(i) # dfs 실행
        C_cnt += 1 # 서로 다른 구역을 탐색하기 때문에 카운트 증가

print(C_cnt)