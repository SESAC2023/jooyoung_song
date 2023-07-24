t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    floor = [x for x in range(1, n+1)]
    for i in range(1, k+1):
        for j in range(1, n):
            floor[j] += floor[j-1]
    print(floor[-1])
