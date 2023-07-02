import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_list = set()
M_list = set()

for _ in range(N):
    N_list.add(input().rstrip())
for i in range(M):
    M_list.add(input().rstrip())
  

answer = sorted(list(N_list & M_list)) # 교집합
print(len(answer))

for name in answer:
    print(name)

