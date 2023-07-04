import sys
input = sys.stdin.readline

N = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

# 처음 거리와 기름값을 곱해 최소 비용에 추가
min_price = dist[0] * cost[0]

# 가장 값이 싼 주유소 지정
min_cost = cost[0]

# 지금까지의 주유 가격보다 이번 도시의 가격이 작으면
# 지금까지의 지났던 주유소의 리터당 가장 작은 값으로 이동
# 최소 주유소 가격을 갱신하면서 이동
for i in range(1, N-1):
    if min_cost > cost[i]:
        min_cost = cost[i]
    min_price += min_cost * dist[i]

print(min_price)
