N = int(input())

def prime_factors(n):
    factors = []
    i = 2

    while i*i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1

    if n > 1:
        factors.append(n)

    return factors

for num in prime_factors(N):
    print(num)
