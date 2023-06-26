import sys
input = sys.stdin.readline
N, M = list(map(int, input().split()))

count = []
temp = N

while(1):
    if temp < M:
        count.append(temp)
        break
    count.append(temp % M)
    temp = temp //M

for i in reversed(range(len(count))):
    if count[i] < 10:
        print(count[i], end = '')
    else:
        print(chr(count[i]+55), end= '')
