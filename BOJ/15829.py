r = 1
M = 1234567891
hash = 0
count = 0

n = int(input())
String = list(map(ord, input()))

for i in range(n):
    hash += (String[i]-96)*r
    r *= 31

print(hash)
