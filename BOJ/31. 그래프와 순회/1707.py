import sys
input = sys.stdin.readline
from collections import deque

k = int(input())

# 이분 그래프 = 그래프 정점의 집합을 둘로 나눴을 때 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할 가능한 그래프
# = 그래프의 정점을 2개의 집합으로 구분할 때, 인접한 정점끼리는 다른 집합에 속한다.

def bfs(graph, start):
    q=deque()
    q.append(start)
    if visited[start] == 0:
        visited[start] = 1
    while q:
        v = q.popleft()

        flag = visited[v]
        for i in graph[v]: # v정점 연결 정점 체크
          
            if visited[i] == 0: # 방문하지 않은 경우
                q.append(i)     # 큐에 삽입
                if flag == 1:       # 방문하지 않았고 1번 집합인 상태이면 
                    visited[i] = 2  # 현재의 정점과 다른 집합인 2 로 변경
                else:
                    visited[i] = 1  # 그냥 처음 방문하는 경우 집합 1로 변경

            elif visited[i] == 1:   # 방문을 한 경우. 1번 집합으로 설정했던 경우
                if flag == 1:       # 인접 정점도 1번 집합인 경우
                    print('NO')     # 이분 그래프가 아니므로 No 프린트 후 True return
                    return True
            elif visited[i] == 2:   # 방문을 한 경우. 2번 집합으로 설정했던 경우
                if flag == 2:       # 인접 정점도 2번 집합인 경우
                    print('NO')     # 이분 그래프가 
                    return True    # 아니므로 No 프린트 후 True return
    
    return False # while 문에서 return 이 안걸리면 False 반환


for _ in range(k):
    num_V, num_E = map(int, input().split())

    # 그래프
    graph = [[] for _ in range(num_V+1)]
    visited = [0] * (num_V+1)
    print_check = 0
    for _ in range(num_E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # 모든 정점에 대해 BFS
    for i in range(1, num_V + 1):
        if bfs(graph, k):
            print_check = 1
            break

    if print_check == 0:
        print("YES")
