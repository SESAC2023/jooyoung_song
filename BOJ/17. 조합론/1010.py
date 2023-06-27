import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

T = int(input())
site = []
for _ in range(T):
    n, m = map(int, input().split())
    site.append([n, m])

# 답은 mCn, 이전 11050번 조합 계산 코드를 가져와서 변수 이름이 다를 수 있음
for x in range(T):
    N, M = site[x]

    nf = 1
    nkf = 1
    kf = 1
    
    for i in range(1,M+1):
        nf *= i

    for j in range(1, M-N+1):
        nkf *= j

    for z in range(1, N+1):
        kf *= z

    print(nf // (nkf * kf))
