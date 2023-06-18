data = list(map(int, input().split()))
h = data[0]
m = data[1]
n = int(input())

hour = n // 60
min = n % 60

# 시 설정
if h + hour > 23:  # 24시 넘어가는 경우
  hour = h + hour - 24  # 00시 부터 초기화
else:
  hour = h + hour

# 분 설정
if m + min > 59:  # 60분 넘어가는 경우
  min = m + min - 60  # 00분 부터 초기화
  hour += 1  # 시 1 증가
  if hour == 24:
    hour = hour - 24
else:
  min = m + min

print(hour, end=" ")
print(min)
