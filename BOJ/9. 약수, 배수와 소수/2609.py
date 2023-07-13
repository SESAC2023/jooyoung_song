# 두 수를 입력 받아 최소공배수와 최대공약수 출력

a, b = map(int,input().split())

gcd = a
tb = b

while tb != 0:
    temp = gcd % tb
    gcd = tb
    tb = temp

print(gcd)
print((a*b)//gcd)
