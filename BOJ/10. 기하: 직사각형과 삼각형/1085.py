x, y, w, h = list(map(int, input().split()))

#x, y, w-x, h-y 4개 값 중 최소값 출력

x_dist = w-x
y_dist = h-y

dist = []
dist.append(x)
dist.append(y)
dist.append(x_dist)
dist.append(y_dist)

print(min(dist))
