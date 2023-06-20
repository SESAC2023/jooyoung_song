data = []
for i in range(10):
    data.append(int(input())%42)

set = set(data) #set은 중복요소를 허용하지 않는 데이터 타입
print(len(set))
