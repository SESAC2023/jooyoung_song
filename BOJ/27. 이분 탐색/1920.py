import sys
input = sys.stdin.readline

n = int(input())
A = set(map(int, input().split()))

m = int(input())
B = list(map(int, input().split()))

for b in B:
    if b in A:
        print(1)
    else:
        print(0)

      
# 나중에 이분 탐색으로도 풀어보기
