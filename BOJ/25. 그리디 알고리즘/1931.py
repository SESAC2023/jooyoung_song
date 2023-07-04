import sys
input = sys.stdin.readline

N = int(input())
time = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 빨리 끝나는 회의부터 정렬 -> 끝나는 시간 오름차순
# 끝나는 시간이 같은 경우 -> 시작하는 시간 오름차순
time.sort(key = lambda x: (x[1], x[0]))

cnt = 0
end_time = 0
for start, end in time:
    if end_time <= start:
        end_time = end
        cnt += 1

print(cnt)
