n = int(input())

inc = 0
temp = 1
while(1):
    if n <= inc:
        break
    inc += temp
    temp += 1

if inc - n == 0 and temp % 2 == 0:
    print(f"1/{temp - 1}")

elif inc - n == 0 and temp % 2 == 1:
    print(f"{temp - 1}/1")

elif temp % 2 == 0:
    print(f"{inc - n + 1}/{temp - (inc - n + 1)}")

else:
    print(f"{temp - (inc - n + 1)}/{inc - n + 1}")
