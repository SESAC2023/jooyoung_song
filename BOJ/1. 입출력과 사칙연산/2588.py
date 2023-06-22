a1 = int(input())
a2 = int(input())

print(a1*(a2%10))
print(a1*(((a2%100)-(a2%10))//10))
print(a1*((a2-(a2%100))//100))
print(a1*a2)
