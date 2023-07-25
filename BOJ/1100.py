import sys
input = sys.stdin.readline

board = []
count = 0

for _ in range(8):
    board.append(input().rstrip())

for i in range(8):
    for j in range(8):
        if (i+j) %2 == 0 and board[i][j] == 'F':
            count += 1

print(count)
