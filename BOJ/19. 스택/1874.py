import sys
input = sys.stdin.readline

N = int(input())
stack = [] 
start = 1
operator = []
flag = False

for _ in range(N):
    end = int(input())
    while start <= end: # 시작지점부터 입력받은 지점까지
        stack.append(start) 
        # 스택에 push (가장 먼저 꺼내려면 오름차순 push)
        operator.append('+')
        # 연산자 스택에 + 저장
        start += 1
        # 시작지점 업데이트

    # 다 넣었으면 빼서 만들 수 있는가 체크
    if stack[-1] == end : # 만약 스택 마지막 항이 end랑 같을 경우
        stack.pop() #마지막 부분 꺼냄
        operator.append('-')

    # 못 만드는 경우
    else : #end랑 다를 경우
        print("NO")
        flag = True
        break


if not flag:
    for i in operator :
        print(i)
