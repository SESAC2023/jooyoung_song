word = input().upper()
unique = list(set(word))

count_list = []
for i in unique:
    count = word.count(i)
    count_list.append(count)

if count_list.count(max(count_list)) > 1:
    print('?')
else:
    max_index = count_list.index(max(count_list))
    print(unique[max_index])

"""
counter = dict()

data = input()

#전형적인 카운터(Counter) 구현
for x in data:
    if x not in counter:
        counter[x]=1
    else:
        counter[x] += 1

#딕셔너리 순회
#for (key, value) in counter.items():
#    print(key, value)

max_cnt = 0
max_char = 'a'
for (key, value) in counter.items():
    if value > max_cnt:
        max_char = key
        if value == max_cnt:
            cnt += 1

cnt = 0
for (key, value) in counter.items():
    if value > max_cnt:
        max_char = key
        if value == max_cnt:
            cnt += 1

if cnt >= 2:
    print('?')
else:
    print(max_char)

"""
