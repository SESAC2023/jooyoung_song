N = int(input())

list = []

count = N - len(str(N))*9
if count < 0:
    count = 1

while(1):
    cr = count
    create = []
    while(1):    
        create.append(cr % 10)
        cr //= 10
        if cr == 0:
            break
    if (count + sum(create)) == N:
        print(count)
        break
    count += 1
    if count >= N:
        print('0')
        break        
