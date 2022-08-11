import sys
sys.stdin = open("2606.txt")

# 인풋 받기
n=int(input())
m=int(input())
# 빈 인접리스트 생성
graph=[[] for _ in range(n+1)]
# 인접 리스트 append
for _ in range(m):
    x,y=map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
# 방문기록 생성
visit=[False for _ in range(n+1)]
# dfs 함수 선언
def dfs(start):
    visit[start]=True
    for i in graph[start]:
        if visit[i] == False:
            dfs(i)
# 함수 실행
dfs(1)
# 결과값출력
print(visit.count(True)-1)
#햐아 내가 해냇어 ~!