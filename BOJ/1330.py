arr = list(map(int,input().split()))
A=arr[0]
B=arr[1]
if A > B:
  print(">")
elif A < B:
  print("<")
else:
  print("==")
