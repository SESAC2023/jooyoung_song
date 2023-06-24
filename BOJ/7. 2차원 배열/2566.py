array = [[]*9 for _ in range(9)]
for i in range(9):
    array[i] = list(map(int,input().split()))

max = -1 # 0으로 설정했었을 때 틀림
max_x = -1
max_y = -1
for i in range(9):
    for j in range(9):
        if max < array[i][j]:
            max = array[i][j]
            max_x = i+1
            max_y = j+1

print(max)
print(f"{max_x} {max_y}")
