import sys
input = sys.stdin.readline

N = int(input())
num = []
for _ in range(N):
    num.append(int(input()))

num.sort()

for n in num:
    print(n)
