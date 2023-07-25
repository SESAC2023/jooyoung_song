import sys
input = sys.stdin.readline

num = list(str(input().rstrip()))
flag = 0

for i in num:
    i = int(i)
    binary = []
    while True:
        if i == 0:
            break
        binary.append(i % 2)
        i //= 2
    while len(binary) != 3:
        binary.append(0)
    binary.reverse()
  
    for j in binary:
        if j == 1:
            flag = 1
        if flag == 1:
            print(j, end='')

# 입력이 0인 경우
if flag == 0:
    print(0)

'''
# 동작은 맞으나 시간초과 나는 코드. 십진수로 변환후 이진수 변환
decimal = 0
power = 1

for i in range(len(num)):
    decimal += int(num[len(num) - i - 1]) * power
    power *= 8

# print(decimal)

binary = []
while True:
    if decimal == 0:
        break
    binary.append(decimal % 2)
    decimal //= 2

binary.reverse()
for i in binary:
    print(i, end='')
'''
