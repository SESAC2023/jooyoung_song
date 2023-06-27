N = int(input())
x_point = []
y_point = []

for _ in range(N):
    x, y = (map(int, input().split()))
    x_point.append(x)
    y_point.append(y)

print((max(x_point) - min(x_point))*(max(y_point)-min(y_point)))
