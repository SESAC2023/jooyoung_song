import sys
input = sys.stdin.readline

n = input().rstrip()
f = int(input())

# 맨 뒤 자리 빼고 입력받아 00붙이고
num = int(n[:-2] + '00')

# 1씩 증가시키면서 체크
while True:
    if num % f == 0:
        break
    num += 1

# 마지막 2자리 출력
print(str(num)[-2:])
