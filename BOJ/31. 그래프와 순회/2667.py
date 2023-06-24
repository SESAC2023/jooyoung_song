import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

N = int(input())
array = [[]*N for i in range(N)]
visited = [[]*N for i in range(N)]

for i in range(N):
    array[i] = list(input().rstrip())

print(array)
