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
    
        
