T=int(input())

for i in range(1, T+1):
    for j in range(1, T+1):
        if(j <= T-i):
            print(' ', end='')
        else:
            print('*', end='')
  

    print('')
