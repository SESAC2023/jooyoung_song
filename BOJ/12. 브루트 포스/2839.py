N = int(input())
flag = 0

for i in range(0, (N//3) + 1):
    if flag == 1:
        break
    for j in range(0, (N//5) + 1):
        m = 3*i + 5*j
        if m == N:
            flag = 1
            print(i+j)
            break

if flag == 0:
    print(-1)
