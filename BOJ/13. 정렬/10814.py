import sys
input = sys.stdin.readline

N = int(input())

info = []
for _ in range(N):
    age, name = input().split()
    age = int(age)
    info.append((age, name))

info.sort(key = lambda x : x[0])

for i in range(N):
    print(f'{info[i][0]} {info[i][1]}')
