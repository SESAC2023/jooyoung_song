n = int(input())

for _ in range(n):
    quiz = list(str(input()))
    length = len(quiz)
    score = 0
    flag = 0
    temp = 0
    for i in range(length):
        if quiz[i] == 'O' and flag == 0:
            flag = 1
            temp = 1
            score += 1
        elif quiz[i] == 'O' and flag == 1: 
            temp += 1
            score += temp
          
        if quiz[i] == 'X':
            flag = 0
            temp = 0
    print(score)
