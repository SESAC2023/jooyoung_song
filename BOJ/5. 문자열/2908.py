N, M = list(map(int,input().split()))

N = int(str(N)[::-1])
M = int(str(M)[::-1])

if N > M:
    print(N)
else:
    print(M)
