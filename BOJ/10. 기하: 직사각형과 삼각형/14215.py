len = list(map(int, input().split()))

len.sort()
temp = len[0]+len[1]

if temp <= len[2]:
    print(temp + temp - 1)
else:
    print(temp + len[2])
