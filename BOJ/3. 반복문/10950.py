count = int(input())
result = []

for i in range(count):
    a, b = list(map(int,input().split()))
    result.append(a+b)

for j in result:
    print(j)
