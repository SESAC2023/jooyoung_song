N, M = list(map(int, input().split()))

basket = [i for i in range(1,N+1)]

for _ in range(M):
    i, j = list(map(int, input().split()))
    basket[i-1:j]=reversed(basket[i-1:j])

for i in basket:
    print(i, end=" ")
