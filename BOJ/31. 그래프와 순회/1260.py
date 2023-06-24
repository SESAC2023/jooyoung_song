import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))


N, M, V = list(map(int,input().split()))


graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    i.sort()

def dfs(x):
    global count
    visited[x] = True
    print(x, end=' ')
    for y in graph[x]:
        if not visited[y]:
            dfs(y)

dfs(V)

visited = [False] * (N+1)
print()

q = deque()
q.append(V)
visited[V] = True



while q:
    x = q.popleft()
    print(x, end= ' ')
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            q.append(i)


    
