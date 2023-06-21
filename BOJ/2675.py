n = int(input())

for _ in range(n):
    count, word = input().split()
    for i in word:
        print(i*int(count), end='')
    print()
    
