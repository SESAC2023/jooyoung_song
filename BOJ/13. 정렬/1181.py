import sys
input = sys.stdin.readline

N = int(input())

words = []

for _ in range(N):
    ch = input().rstrip()
    words.append(ch)

# 중복 요소 제거
set_words = set(words)
words = list(set_words)

words.sort()
words.sort(key = len)

for word in words:
    print(word)
