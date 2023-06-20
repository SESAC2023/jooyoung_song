N, M = list(map(int, input().split()))
basket = []

for a in range(N):
    basket.append(0)

for j in range(M):
    i, j, k = list(map(int, input().split()))

    for b in range(i, j+1):
        basket[b-1] = k

for c in basket:
    print(c, end= ' ')
