import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    m = input().split()
    if m[0] == 'push':
        stack.append(m[1])
    elif m[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else: print(stack.pop())
    elif m[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif m[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else: 
            print(stack[len(stack)-1])
    elif m[0] == 'size':
        print(len(stack))
