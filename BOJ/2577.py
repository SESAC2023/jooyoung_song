num_list = [0 for _ in range(10)]
num = 1

for _ in range(3):
    num *= int(input())

while True:
    num_list[num % 10] += 1
    num //= 10
    if num == 0:
        break

for cnt in num_list:
    print(cnt)
    
