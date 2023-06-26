N, K = map(int, input().split())

measure=[]
flag = 0

for i in range(1, N+1):
    if N % i == 0:
        measure.append(i)
    if len(measure) == K:
        print(measure[K-1])
        flag = 1
        break

if flag == 0:
    print('0')
