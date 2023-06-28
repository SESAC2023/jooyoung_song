import sys
from collections import deque
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

def BFS(x, y):
    q = deque()
    q.append((x,y))

    while q:
        x, y = q.popleft()
        if x==end_x and y==end_y:
            print(matrix[x][y])
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= l or ny >= l:   
                continue
            if matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                q.append((nx,ny))

T = int(input())
for _ in range(T):
    l = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    matrix = [[0]*l for _ in range(l)]

    BFS(start_x,start_y)
