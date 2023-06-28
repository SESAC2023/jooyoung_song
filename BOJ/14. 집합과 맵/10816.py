N = int(input())
cards = list(map(int, input().split()))

counter = dict()
for x in cards:
    if x not in counter:
        counter[x] = 1
    else:
        counter[x] += 1

M = int(input())
check = list(map(int, input().split()))

answer = 0

for num in check:
    if num in counter:
        print(counter[num], end= ' ')
    else:
        print(0, end=' ')
