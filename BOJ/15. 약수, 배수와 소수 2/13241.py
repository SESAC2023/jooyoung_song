def gcd(a, b):
    while b != 0 :
        r = a % b
        a = b
        b = r
    return a

A, B = map(int, input().split())
print(int((A*B / gcd(A,B))))
