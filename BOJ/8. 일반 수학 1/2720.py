T = int(input())
change_list = []

for _ in range(T):
    change = int(input()) / 100
    change_list.append(change)

quarter = 0.25
dime = 0.1
nickel = 0.05
penny = 0.01

for i in range(T):
    print(int(change_list[i] // quarter), end=' ')
    change_list[i] %= quarter
    change_list[i] = round(change_list[i], 3)
    print(int(change_list[i] // dime), end=' ')
    change_list[i] %= dime
    change_list[i] = round(change_list[i], 3)
    print(int(change_list[i] // nickel), end=' ')
    change_list[i] %= nickel
    change_list[i] = round(change_list[i], 3)
    print(int(change_list[i] / penny), end=' ')
    print()
