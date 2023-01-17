n, m = map(int, input().split())
num_list = list(map(int, input().split()))

low = 1
high = sum(num_list)

def Count(capacity):
    cnt = 1
    sum = 0
    for x in num_list:
        if sum + x > capacity:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt


while low <= high:
    mid = (low + high) // 2
    if Count(mid) <= m:
        res = mid
        high = mid - 1
    else:
        low = mid + 1
print(res)