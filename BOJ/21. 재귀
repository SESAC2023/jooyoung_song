import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

N = int(input())
result = 0

def factorial(n):
    if n == 1 or n == 0:
        result = 1
    if n >= 2:
        result = n*factorial(n-1)
    return result

print(factorial(N))
