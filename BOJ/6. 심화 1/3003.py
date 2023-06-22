piece_list = [1, 1, 2, 2, 2, 8]

white_piece = list(map(int,input().split()))

for i in range(6):
    piece_list[i] = piece_list[i] - white_piece[i]

for cnt in piece_list:
    print(cnt)
