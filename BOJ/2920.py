syllable = list(map(int, input().split()))

cnt = 0

for i in range(1, 8):
    if syllable[i-1] == (syllable[i] - 1):
        cnt += 1

if cnt == 7:
    print("ascending")
else:
    cnt = 0
    for i in range(1, 8):
        if syllable[i-1] == (syllable[i] + 1):
            cnt += 1

    if cnt == 7:
        print("descending")

    else:
        print("mixed")
    
        
"""
# 더 좋은 풀이

a = list(map(int, input().split()))
 
if a == sorted(a):
    print('ascending')
elif a == sorted(a, reverse=True):
    print('descending')
else:
    print('mixed')

"""
