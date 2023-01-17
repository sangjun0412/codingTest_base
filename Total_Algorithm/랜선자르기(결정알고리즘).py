k, n = map(int, input().split())
num_list = []
for _ in range(k):
    num_list.append(int(input()))

num_list.sort()
low = 1
high = num_list[-1]
res = 0

while low <= high:
    mid = (low + high) // 2
    tmp = 0
    for num in num_list:
        tmp += num // mid
    if tmp >= n:
        res = mid
        low = mid + 1
    elif tmp < n:
        high = mid - 1

print(res)