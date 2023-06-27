import sys
input = sys.stdin.readline

N = int(input())

dots = []

for _ in range(N):
    x, y = map(int, input().split())
    dots.append([y, x])

sorted_dots= sorted(dots)

for i in range(N):
    print(f'{sorted_dots[i][1]} {sorted_dots[i][0]}')
