import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

M, N = map(int, input().split())
graph = [[] for _ in range(N)]
# 방문처리 및 거리값 기록 배열
# -1인 경우 방문하지 않은 위치, 나머지 값은 최단 거리
visited = [[-1]*M for _ in range(N)]

for i in range(N):
    graph[i] = list(map(int, input().split()))

q = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1: # 익은 토마토
            q.append((i,j))
            visited[i][j] = 0

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if graph[nx][ny] == -1:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = 1
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx,ny))

possible = True
answer = 0
for i in range(N):
    for j in range(M):
        #도착 불가능하면서 벽이 아닌 경우
        if visited[i][j] == -1 and graph[i][j] != -1:
            possible = False
        # answer 에는 최댓값이 담긴다.
        answer = max(answer, visited[i][j])

if possible:
    print(answer)
else:
    print(-1)
    
    
    
