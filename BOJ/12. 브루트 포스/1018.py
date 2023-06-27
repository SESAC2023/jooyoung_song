N, M = map(int, input().split())

chess = [[] for _ in range(N)]
count = []

for i in range(N):
    chess[i] = list(input())

# 체스판 경우의 수 2가지 모두 성립하는 규칙
# 시작점의 좌표의 합이 짝수라면 합이 짝수인 인덱스는 모두 시작점과 같은 색
# 시작점의 좌표의 합이 홀수라면 합이 홀수인 인덱스는 모두 시작점과 같은 색

for a in range(N-7):
    for b in range(M-7):
        W = 0 # 흰색 시작 색칠 횟수
        B = 0 # 검정 시작 색칠 횟수
        for i in range(a, a+8): # 시작지점
            for j in range(b, b+8): # 시작지점
                if (i+j)%2 == 0: # 짝수
                    if chess[i][j] != 'W': # B이면
                        W += 1
                    else:
                        B += 1
                else: # 홀수
                    if chess[i][j] != 'W': # W이면
                        B += 1
                    else:
                        W += 1
        count.append(W)
        count.append(B)

print(min(count))
