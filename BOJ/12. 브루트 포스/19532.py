a, b, c, d, e, f = map(int, input().split())

value = []

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x+b*y == c:
            value.append([x, y])

for xy in value:
    if d*xy[0] + e*xy[1] == f:
        print(f'{xy[0]} {xy[1]}')
