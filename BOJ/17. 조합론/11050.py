N, K = map(int, input().split())
nf = 1
nkf = 1
kf = 1

for i in range(1,N+1):
    nf *= i

for j in range(1, N-K+1):
    nkf *= j

for z in range(1, K+1):
    kf *= z

print(nf // (nkf * kf))
