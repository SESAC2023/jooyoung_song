import sys
input = sys.stdin.readline

k, n = map(int, input().split())

lan = []

for _ in range(k):
    lan.append(int(input()))

# 이진 탐색 시작점 끝점
start = 1
end = max(lan)

while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in lan:
        total += x // mid # 분할 된 랜선 수

    # 랜선 개수가 분기점
    if total >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)
