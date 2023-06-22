count = int(input())
result=[]

for i in range(count):
    a, b = list(map(int, input().split()))
    result.append(a+b)

for j in range(count):
    print(f"Case #{j+1}: {result[j]}")
