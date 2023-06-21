N=int(input())
data = []
for _ in range(N):
    string = list(input())
    data.append(string[0]+string[-1])

for i in range(N):
    print(data[i])
