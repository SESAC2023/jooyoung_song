N, M = list(map(int, input().split()))

count = []
temp = N
cnt2 = 0

for _ in range(5):
    cnt = 0
    
    while(1):
        temp = temp // M
        print(temp)
        cnt += 1
        if temp == 0:
            count.append(cnt)
            cnt2 = cnt
            break
    temp = N - (M*cnt2)
    print(cnt2)
    if temp == 0:
        break


print(count)



    

"""

for i in range(len(N)):
    N[i] = N[i] - 55
    if N[i] < 3: # 0 ~ 9를 그대로 나타내기 위한 조건
        N[i] += 7

temp = len(N) - 1

for i in range(len(N)):
    for _ in range(temp):
        N[i] *= M
    temp -= 1

result = 0
for j in range(len(N)):
    result += N[j] 

print(result)
"""
