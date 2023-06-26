A, B, V = map(int, input().split())

least_count = (V - A) // (A - B)

V -= least_count * (A-B)

while(1):
    least_count += 1
    V -= A
    if V <= 0:
        break
    V += B

print(least_count)
