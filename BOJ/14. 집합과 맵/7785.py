import sys
input = sys.stdin.readline

N = int(input())
name = dict()

for _ in range(N):
    a, b = map(str, input().split())
    if b == 'enter':
        name[a] = b
    else:
        del name[a]

name = sorted(name.keys(), reverse = True)

for i in name:
    print(i)
