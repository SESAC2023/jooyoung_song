import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

N, M = map(int, input().split())
answer = []

def backtracking(start):
    # M개의 원소를 가진 경우 출력 후 종료
    if len(answer)==M:
        print(' '.join(map(str,answer)))
        return

    for i in range(start, N+1):
        answer.append(i) 
        backtracking(i)
        answer.pop()
          
backtracking(1)
