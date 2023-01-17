n = int(input())
result = 0
for i in range(1, n+1):
    sum = 0
    for j in str(i):
        sum += int(j)
    result = i + sum
    if(result == n):
        print(i)
        break
    if i == n:
        print(0)
