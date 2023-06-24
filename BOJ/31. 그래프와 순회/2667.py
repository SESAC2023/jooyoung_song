import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
array = [[]*N for i in range(N)]
visited = [[False]*N for i in range(N)]

for i in range(N):
    array[i] = list(map(int, input().rstrip()))

num = 0
answer_list = []

def dfs(x, y):
    global num
    global count
    array[x][y] = num
    visited[x][y] = True
    count += 1
    for i in range(4):
        if x+dx[i] < N and x+dx[i] >= 0 and y+dy[i] < N and y+dy[i] >= 0:
           nx = x+dx[i]
           ny = y+dy[i]
          
           if array[nx][ny] == 1 and not visited[nx][ny]:
               dfs(nx, ny)

for i in range(N):
    for j in range(N):
        if array[i][j] == 0:
            continue
        if not visited[i][j]:
            num += 1
            count = 0
            dfs(i, j)
            answer_list.append(count)
          
print(num)
for i in answer_list:
    print(i)
