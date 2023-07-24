n, m = map(int, input().split())
castle = []

for _ in range(n):
    castle.append(input())

col, row = 0, 0

# 경비원이 없는 행의 개수
for i in range(n):
    if "X" not in castle[i]:
        col += 1

# 경비원이 없는 열의 개수
for j in range(m):
    if "X" not in [castle[i][j] for i in range(n)]:
        row += 1

# 둘 중 큰 수가 경비원 배치해야하는 최소의 수
print(max(row, col))
