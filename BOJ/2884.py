data = list(map(int,input().split()))
h = data[0]
m = data[1]

if m >= 45:
    print(h, end=" ")
    print( m-45 )
else:
    if h == 0:
        print(23, end=" ")
        print(m+15)
    else:
        print(h-1, end=" ")
        print(m+15)

