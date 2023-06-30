import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

N, M = map(int, input().split())
answer = []

def backtracking():
    # M개의 원소를 가진 경우 출력 후 종료
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return

    for i in range(1, N+1):
        if i not in answer:
            answer.append(i) 
            backtracking()
            answer.pop()
          
backtracking()
