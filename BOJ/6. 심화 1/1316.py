N = int(input())
count = 0
for _ in range(N):
    word = input()
    flag = 0
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            new_word = word[i+1:]
            if new_word.count(word[i]) > 0:
                flag = 1
    if flag == 0:
        count += 1

print(count)
