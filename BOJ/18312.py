n, k = map(int, input().split())
cnt = 0

for hour in range(n+1):
    for min in range(60):
        for sec in range(60):
            hour = str(hour).zfill(2)
            min = str(min).zfill(2)
            sec = str(sec).zfill(2)
            current = hour + min + sec
            if str(k) in current:
                cnt += 1

print(cnt)
