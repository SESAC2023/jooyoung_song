data = input()
data = data.split(" ")
data = list(map(int, data))
A = data[0]
B = data[1]
C = data[2]
print( (A+B)%C )
print( ((A%C)+(B%C))%C )
print( (A*B)%C )
print( ((A%C)*(B%C))%C )
