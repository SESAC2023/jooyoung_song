ans = []
while(1):

    a, b = list(map(int, input().split()))

    if (a+b != 0):
        ans.append(a+b)

    if a == 0 and b == 0:
        break
      
for i in ans:
    print(i)
