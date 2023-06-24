import sys
from collections import deque
input = sys.stdin.readline

N, M, R = list(map(int, input().split()))

graph = [[] for _ in range(N+1)]
answer = [0] * (N+1)
visited = [False] * (N+1)

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

order = 1

for i in range(len(graph)):
    graph[i].sort()

#BFS 메소드 정의
def bfs(start):
    global order
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        answer[v] = order
        order += 1
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

bfs(R)

for i in range(1, N+1):
    print(answer[i])
