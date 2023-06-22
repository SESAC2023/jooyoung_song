import sys
result = []

T=int(sys.stdin.readline().rstrip())

for i in range(T):
    a, b = list(map(int, sys.stdin.readline().rstrip().split()))
    result.append(a+b)

for j in range(T):
    print(result[j])
