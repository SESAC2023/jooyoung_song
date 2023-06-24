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

print(array)

num = 3

#테스트
print()
print(array[1][1])
print(visited[1][1])
print()
#테스트


def dfs(x, y):
    global num
    array[x][y] = num
    visited[x][y] = True
    for i in range(4):
        if x+dx[i] < N and x+dx[i] > 0 and y+dy[i] < N and y+dy[i] > 0:
           nx = x+dx[i]
           ny = y+dy[i]
          
           # 테스트
           print()
           print(f"nx={nx}, ny = {ny}")
           print()
           #
          
           if array[nx][ny] == 1 and not visited[nx][ny]:
               # 테스트
               print("DFS 체크")
               dfs(nx, ny)

"""
for i in range(N):
    for j in range(N):
        visited = [[False]*N for i in range(N)]
        dfs(i, j)
        if pass
        
"""   
dfs(0,1)
print(array)
print(visited)
