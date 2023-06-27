N, M = map(int, input().split())

chess = [[] for _ in range(N)]
count = []

for i in range(N):
    chess[i] = list(input())

# 체스판 경우의 수 2가지 모두 성립하는 규칙
# 시작점의 좌표의 합이 짝수라면 합이 짝수인 인덱스는 모두 시작점과 같은 색
# 시작점의 좌표의 합이 짝수인 상태에서 합이 홀수인 인덱스는 모두 반대 색이어야 한다.
# > 모든 8*8에 대해 브루트 포스

for a in range(N-7):
    for b in range(M-7):
        W = 0 # 흰색 색칠 횟수
        B = 0 # 검정 색칠 횟수
        # 한 시작점에서 W+B 는 항상 64가 된다.
        for i in range(a, a+8): # 시작지점
            for j in range(b, b+8): # 시작지점            
                if (i+j)%2 == 0: # 짝수
                    if chess[i][j] != 'W': # B이면
                        W += 1
                    else:                  # W라면
                        B += 1
                else: # 홀수
                    if chess[i][j] != 'W': # B이면
                        B += 1
                    else:                  # W라면
                        W += 1
        count.append(W)
        count.append(B)

print(min(count))
