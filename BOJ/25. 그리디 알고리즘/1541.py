import sys
input = sys.stdin.readline

# 최초로 마이너스가 나오기 전까지는 숫자를 모두 더해야 하고, 이후 마이너스가 나오는 순간 그 뒤에 모든 수를 뺀다.
s = list(input().rstrip().split('-'))
sum = 0 # 총합 계산
#print(s)
for i in s[0].split('+'):
    sum += int(i)

for i in s[1:]:
    for j in i.split('+'):
        sum -= int(j)

print(sum)
