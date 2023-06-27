N = int(input())

num_list = list(map(int, input().split()))
count = 0

def prime_cheaker(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
            
for num in num_list:
    if prime_cheaker(num):
        count += 1

print(count)
