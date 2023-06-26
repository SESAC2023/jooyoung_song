n = int(input())

cnt = 1
bound = 1

while(1):
    if bound >= n:
        break
    bound += 6*cnt
    cnt += 1

print(cnt)
