import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline
N, M, R = list(map(int, input().split()))

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
answer = [0] * (N+1)

for i in range(M):
    u, v = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)
  
order = 1

for adjacent in graph:
    adjacent.sort(reverse=True)

def dfs(v):
    global order
    visited[v] = True
    answer[v] = order
    order += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

dfs(R)

for i in range(1, N+1):
    print(answer[i])
    
    
