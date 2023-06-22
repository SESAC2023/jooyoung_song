N = int(input())

for i in range(1, N+1):
    print(' '*(N-int(i)) + '*'*(2*int(i)-1))

for j in range(1, N):
    print(' '*(int(j)) + '*'*((2*N-1)-2*int(j)))
