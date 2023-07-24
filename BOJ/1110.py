n = list(map(int, (str(input()))))
if len(n) == 1:
    n.insert(0, 0)
initial = n[0]*10 + (n[1] % 10)
count = 0

while True:
    n.append((n[0]+n[1])%10)
    n.pop(0)
    count += 1
    check = n[0]*10 + (n[1] % 10)
    if initial == check:
        break

print(count)
