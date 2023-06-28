import sys
from collections import deque
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(x,y):
    q = deque()
    q.append((x,y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
              
            if arr[nx][ny] == 1:
                q.append((nx,ny))
                arr[nx][ny] = 0

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    
    arr = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    
    for _ in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                BFS(i,j)
                count += 1
              
    print(count)
    
                
