import sys
input = sys.stdin.readline

S = []
count = 0

N, M = map(int, input().split())
for _ in range(N):
    S.append(input())

S = set(S)

for _ in range(M):
    ch = input()
    if ch in S:
        count += 1

print(count)
