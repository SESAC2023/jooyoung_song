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
