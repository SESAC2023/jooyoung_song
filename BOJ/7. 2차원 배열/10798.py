array = [list(input()) for _ in range(5)]
length = []

for k in range(5):
    length.append(len(array[k]))

for j in range(max(length)):
    for i in range(5):
        if j < len(array[i]):
            print(array[i][j], end='')
