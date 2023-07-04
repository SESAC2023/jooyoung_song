import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

N, M = map(int, input().split())
answer = []

def backtracking():
    # M개의 원소를 가진 경우 출력 후 종료
    if len(answer) == M:
        for i in range(M):
            print(answer[i], end=' ')
        print('')
        return

    for i in range(1, N+1):
        answer.append(i) 
        backtracking()
        answer.pop()
          
backtracking()
