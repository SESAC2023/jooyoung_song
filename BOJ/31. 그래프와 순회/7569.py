import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# 방문처리 및 거리값 기록 배열
# -1인 경우 방문하지 않은 위치, 나머지 값은 최단 거리
visited = [[[-1]*M for _ in range(N)] for _ in range(H)]

q = deque()
for k in range(H):
    for i in range(N):
        for j in range(M):
            if graph[k][i][j] == 1: # 익은 토마토
                q.append((k,i,j))
                visited[k][i][j] = 0

while q:
    z,x,y = q.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M or nz < 0 or nz >= H:
            continue
        if graph[nz][nx][ny] == -1:
            continue
        if graph[nz][nx][ny] == 0:
            graph[nz][nx][ny] = 1
            visited[nz][nx][ny] = visited[z][x][y] + 1
            q.append((nz,nx, ny))

possible = True
answer = 0

for k in range(H):
    for i in range(N):
        for j in range(M):
            #도착 불가능하면서 벽이 아닌 경우
            if visited[k][i][j] == -1 and graph[k][i][j] != -1:
                possible = False
            # answer 에는 최댓값이 담긴다.
            answer = max(answer, visited[k][i][j])

if possible:
    print(answer)
else:
    print(-1)
