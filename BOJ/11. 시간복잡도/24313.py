a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())


# a1 <= c 반례 : a1 = 4, a0 = -2, c = 2, n0 = 2
if (a1*n0 + a0) <= (c*n0) and a1<=c:
    print(1)
else:
    print(0)
