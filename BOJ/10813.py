N, M = list(map(int, input().split()))
basket = []

for a in range(1, N+1):
    basket.append(a)

for b in range(M):
    i, j = list(map(int, input().split()))
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

for c in basket:
    print(c, end= ' ')
