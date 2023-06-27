sum = 0
angle=[]
for i in range(3):
    angle.append(int(input()))
    sum += angle[i]

set_angle = set(angle)


if sum != 180:
    print('Error')
elif len(set_angle) == 1:
    print('Equilateral')
elif len(set_angle) == 2 :
    print('Isosceles')
elif len(set_angle) == 3:
    print('Scalene')
    
