import sys
from collections import deque
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

N, K = map(int, input().split())
max_num = 100000
visited = [0]*100001

def BFS(n):
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()
        # 동생의 위치를 찾았다면 출력 후 종료
        if x==K:
            print(visited[x])
            break
        for i in (x-1, x+1, x*2):
            if 0<=i<=max_num and not visited[i]:
                visited[i] = visited[x] + 1
                q.append(i)

BFS(N)
