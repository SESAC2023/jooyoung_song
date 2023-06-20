data = []
for i in range(9):
    data.append(int(input()))

m = max(data)

print(m)
print(data.index(m) + 1)
