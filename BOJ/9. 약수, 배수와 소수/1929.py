import math

def primenum(x):
    for i in range(2, int(math.sqrt(x) + 1)):   #2부터 제곱근까지 모든 숫자 중
        if x % i == 0:      #하나라도 나눠지면
            return False
    return True         #전부 통과하면 True

low, high = map(int, input().split())

for i in range(low, high+1):
    if primenum(i):
        print(i)
