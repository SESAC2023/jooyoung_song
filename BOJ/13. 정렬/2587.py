num = [0] * 5
for i in range(5):
    num[i] = int(input())

num.sort()
print(sum(num) // 5)
print(num[2])
