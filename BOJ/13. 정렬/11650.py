import sys
input = sys.stdin.readline

N = int(input())

dots = []

for _ in range(N):
    dots.append(list(map(int, input().split())))

sorted_dots= sorted(dots)

for i in range(N):
    print(f'{sorted_dots[i][0]} {sorted_dots[i][1]}')
