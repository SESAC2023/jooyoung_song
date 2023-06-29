import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
visited = [False for _ in range(101)]
ladder = []
snake = []
dice = [i for i in range(1, 7)]

for _ in range(N):
    ladder.append([int(x) for x in input().split()])
for _ in range(M):
    snake.append([int(x) for x in input().split()])

q = deque()
q.append([1,0])
visited[1] = True

while q:
    x, count = q.popleft()

    if x == 100:
        print(count)
        break

    for i in range(6):
        nx = x + dice[i]
        if nx > 100:
            continue

        # 사다리 좌표 도달한 경우. 사다리 좌표의 시작점과 비교
        for j in range(len(ladder)):
            if nx == ladder[j][0] and not visited[nx]:
                visited[nx] = True
                # 연결 시작점에 도달하면 도착점을 큐에 삽입
                q.append([ladder[j][1], count + 1])
              
        # 뱀 좌표 도달한 경우. 뱀 좌표의 시작점과 비교
        for k in range(len(snake)):
            if nx == snake[k][0] and not visited[nx]:  
                visited[nx] = True
                q.append([snake[k][1], count + 1])
              
        # 그냥 도달하지 않은 좌표 간 경우
        if not visited[nx]:
            visited[nx] = True
            q.append([nx, count + 1])
