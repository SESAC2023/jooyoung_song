import sys
input = sys.stdin.readline
input_list = []

while(1):

    N = int(input())
    input_list.append(N)
    if N == -1:
        break


for i in range(len(input_list) - 1):
    N = input_list[i]
    measure=[]

    for i in range(1, N):
        if N % i == 0:
            measure.append(i)

    measure_sum = 0

    for num in measure:
        measure_sum += num
  
    if N == measure_sum:
        print(f'{N} =', end = ' ')
        for num in measure:
            print(num, end = '')
            if num == measure[len(measure)-1]:
                print()
            else:
                print(' + ', end='')
    else:
        print(f'{N} is NOT perfect.')
