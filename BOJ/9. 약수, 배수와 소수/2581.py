M = int(input())
N = int(input())

def prime_cheaker(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

sum = 0
min = 0

for i in range(M, N+1):
    if prime_cheaker(i):
        sum += i
        if min == 0:
            min = i

if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)
