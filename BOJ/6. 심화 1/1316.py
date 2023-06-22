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


"""
def group(string):
    chars = [False] * 26
    # 각 알파벳에 대한 방문 여부
    for i in range(len(string):
        x = ord(string[i]) - 97
        # 방문한 적 없는 알파벳이라면
        if not chars[x]:
            chars[x] = True
        # 방문한 적 있는 알파벳이라면
        else:
            if string[i] != string[i-1]:
                return False
    return True

N = int(input())
cnt = 0
for i in range(N):
    string = input()
    if group(string): cnt += 1
print(cnt)
