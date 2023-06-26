n = int(input())

square = 1
result = 4
ratio = 5

if n == 1:
    print(result + ratio)

else:
    result = 9
    for _ in range(n-1):
        square *= 2
        ratio = int(square*(3*square+2))
        result += ratio
      
    print(result)
