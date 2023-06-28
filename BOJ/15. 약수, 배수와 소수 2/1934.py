T = int(input())

ans = []

def gcd(a, b):
    while b != 0 :
        r = a % b
        a = b
        b = r
    return a

for _ in range(T):
    A, B = map(int, input().split())
    ans.append(A*B / gcd(A,B))

for num in ans:
    print(int(num))
