price = int(input())
count = int(input())
check = 0

for i in range(count):
    a, b = list(map(int, input().split()))
    check += (a*b)

if price == check:
    print("Yes")
else:
    print("No")
