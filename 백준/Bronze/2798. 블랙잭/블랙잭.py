n, m = map(int, input().split())

data_input = list(map(int, input().split()))
data_input.sort()
result = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if data_input[i] + data_input[j] + data_input[k] > m:
                continue
            else:
                result = max(result, data_input[i] + data_input[j] + data_input[k])
print(result)