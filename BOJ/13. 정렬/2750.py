N = int(input())
num_list = []

for _ in range(N):
    num_list.append(int(input()))


# num_list.sort()

# 선택 정렬로 풀어도 시간 초과 통과
for i in range(N):
    least_index = i
    for j in range(i+1, N):
        if num_list[j] < num_list[least_index]:
            least_index = j
    if i != least_index:
        num_list[i], num_list[least_index] = num_list[least_index], num_list[i]
        

for num in num_list:
    print(num)
