import sys
input = sys.stdin.readline

N, M = map(int, input().split())
B = dict()
for i in range(1, N+1):
    a = input().rstrip()
    B[i] = a
    B[a] = i

for i in range(M):
    q = input().rstrip()
    if q.isdigit():
        print(B[int(q)])
    else:
        print(B[q])
