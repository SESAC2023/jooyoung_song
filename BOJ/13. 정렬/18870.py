import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))
sort_X = sorted(set(X))

di = {sort_X[i]:i for i in range(len(sort_X))}

for i in X:
    print(di[i], end = ' ')
