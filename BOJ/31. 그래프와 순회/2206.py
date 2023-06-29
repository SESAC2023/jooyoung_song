import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N)]

for i in range(N):
    graph[i] = list(map(int, str(input().rstrip())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

count = [[0]*M for _ in range(N)]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

q = deque()
q.append((0,0,0))
visited[0][0][0] = 1
possible = False
while q:
    x, y, wall = q.popleft()
    if x == N-1 and y == M-1:
        possible = True
        print(visited[x][y][wall])
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if not visited[nx][ny][wall]:
            if graph[nx][ny] == 0:
                q.append((nx, ny, wall))
                visited[nx][ny][wall] = visited[x][y][wall] + 1
            if wall == 0 and graph[nx][ny] == 1:
                q.append((nx,ny,1))
                visited[nx][ny][1] = visited[x][y][wall] + 1

if not possible:
    print(-1)
