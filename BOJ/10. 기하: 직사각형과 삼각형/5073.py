while(1):
    length = list(map(int, input().split()))
    set_length = set(length)
    if set_length == {0}:
        break

    length.sort()
    if length[2] >= length[0]+length[1]:
        print('Invalid')
    
    elif len(set_length) == 3:
        print('Scalene')
    elif len(set_length) == 2:
        print('Isosceles')
    elif len(set_length) == 1:
        print('Equilateral')
