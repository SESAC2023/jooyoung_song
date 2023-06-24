import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


N, M = list(map(int, input().split()))

array = [[]*M for i in range(N)]
visited = [[False]*M for i in range(N)]


for i in range(N):
    array[i] = list(map(int, input().rstrip()))

q=deque()
q.append((0,0))
visited[0][0] = True

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if array[nx][ny] == 0:
            continue
        if not visited[nx][ny]:
            visited[nx][ny] = True
            q.append((nx, ny))
            array[nx][ny] = array[x][y] + 1
            

print(array[N-1][M-1])
