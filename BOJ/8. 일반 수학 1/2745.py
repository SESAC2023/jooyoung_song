N, M = input().split()
M = int(M)
N = list(map(ord, N))

for i in range(len(N)):
    N[i] = N[i] - 55
    if N[i] < 3: # 0 ~ 9를 그대로 나타내기 위한 조건
        N[i] += 7

temp = len(N) - 1

for i in range(len(N)):
    for _ in range(temp):
        N[i] *= M
    temp -= 1

result = 0
for j in range(len(N)):
    result += N[j] 

print(result)
