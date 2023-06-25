import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
M = int(input())
check_list = list(map(int, input().split()))

num.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in range(M):
    if binary_search(num, check_list[i], 0, N-1) is not None:
        check_list[i] = 1
    else:
        check_list[i] = 0

for element in check_list:
    print(element, end=' ')
