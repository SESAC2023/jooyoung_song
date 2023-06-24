import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

dx = {1, -1, 0, 0}
dy = {0, 0, -1, 1}

N = int(input())
array = [[]*N for i in range(N)]
visited = [[]*N for i in range(N)]

for i in range(N):
    array[i] = list(input().rstrip())

print(array)

def dfs(x, y):
    visited[x][y] = True
    for i in range(3):
        nx = x+dx[i]
        ny = y+dy[i]
        if not visited[nx][ny]:
            dfs(nx, ny)


