c = list(map(int, input().split()))
num = [1,1,2,2,2,8]
result = []

for i in range(len(num)):
    result.append(num[i]-c[i])

for i in result:
    print(i, end=' ')
