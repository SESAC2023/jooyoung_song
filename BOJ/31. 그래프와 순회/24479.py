"""
import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
answer = [0] * (n+1)

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 1

def dfs(x):
    global cnt
    visited[x] = True
    answer[x] = cnt
    cnt+=1
    for y in graph[x]:
        if not visited[y]:
            dfs(y)

for i in range(1, n+1):
    graph[i].sort()

dfs(r)
for i in range(1, n+1):
    print(answer[i])
"""

"""
# 틀린 코드
import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    print(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
  
N, M, R = map(int, input().split(' '))
graph=[[] for _ in range(N+1)]
visited = [False]*(N+1)

for i in range(1, M+1):
    u, v = map(int, input().split(' '))
    graph[u].append(v)
    graph[v].append(u)

for adjacent_list in graph:
    adjacent_list.sort()

dfs(graph, R, visited)
print("0")
"""

# 맞은 코드
import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

order = 1
def dfs(graph, v, visited):
    global order
    visited[v] = True
    answer[v] = order
    order += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
  
N, M, R = map(int, input().split(' '))
graph=[[] for _ in range(N+1)]
visited = [False]*(N+1)
answer = [0] * (N + 1)

for i in range(1, M+1):
    u, v = map(int, input().split(' '))
    graph[u].append(v)
    graph[v].append(u)

for adjacent_list in graph:
    adjacent_list.sort()

dfs(graph, R, visited)

for i in range(1, N + 1):
    print(answer[i])
