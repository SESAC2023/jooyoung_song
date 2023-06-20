T=int(input())
result=[]

for i in range(T):
    data = list(map(int, input().split()))
    result.append(data)
    

for j in range(T):
    print(f"Case #{j+1}: {result[j][0]} + {result[j][1]} = {result[j][0]+result[j][1]}")
