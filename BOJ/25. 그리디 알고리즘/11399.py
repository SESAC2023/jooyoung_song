import sys
input = sys.stdin.readline

N = int(input())
p = list(map(int, input().split()))

p.sort() # 적은 시간 드는 사람부터 계산하면 최솟값
acc = [] # 누적 시간 합을 저장

for i in range(1,N+1):
    acc.append(sum(p[0:i]))

print(sum(acc)) # 전체 시간의 합
