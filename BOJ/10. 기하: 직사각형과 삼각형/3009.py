x_point = []
y_point = []
for _ in range(3):
    x, y =map(int,input().split())
    x_point.append(x)
    y_point.append(y)

x4, y4 = 0, 0

for i in range(3):
    if x_point.count(x_point[i]) == 1:
        x4 = x_point[i]
    if y_point.count(y_point[i]) == 1:
        y4 = y_point[i]

print(f'{x4} {y4}')
