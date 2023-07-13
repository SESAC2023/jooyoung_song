import sys
input = sys.stdin.readline

n = int(input())

factorial = 1

for i in range(2, n+1):
    factorial *= i
# while 문으로 factorial 계산을 하면 왜인지 시간 초과가 발생한다.

factorial = list(map(int, str(factorial)))
factorial = factorial[::-1]

for i in range(len(factorial)):
    if factorial[i] == 0:
        pass
    else:
        cnt = i
        break

print(cnt)
