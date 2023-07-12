from collections import deque

N, K = map(int, input().split())

deq = deque([i for i in range(1, N+1)])

ans = []
while len(deq) != 0:
    for _ in range(K-1):
        #k-1번째 노드까지 deq 맨 뒤로 이동
        deq.append(deq.popleft())
    #k번째 노드 삭제 후 결과에 추가
    ans.append(str(deq.popleft()))

print('<'+', '.join(ans)+'>')
