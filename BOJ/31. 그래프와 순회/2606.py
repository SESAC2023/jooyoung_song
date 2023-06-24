import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
answer = [0] * (N+1)
visited = [False] * (N+1)

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = -1

def dfs(x):
    global count
    visited[x] = True
    count += 1
    for y in graph[x]:
        if not visited[y]:
            dfs(y)

dfs(1)
    
print(count)
