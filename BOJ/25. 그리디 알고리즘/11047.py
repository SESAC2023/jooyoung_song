import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin = []
coin_count = []
for _ in range(N):
    coin.append(int(input()))

count = len(coin) - 1

while(1):
    if K==0:
        break
    coin_count.append(K // coin[count])
    K %= coin[count]
    count -= 1

print(sum(coin_count))
