n = int(input())

first = list(input())
len = len(first)

for i in range(n-1):
    file = list(input())
    for j in range(len):
        if first[j] != file[j]:
            first[j] = '?'

print(''.join(first))
        
