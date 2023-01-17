n, c = map(int, input().split())
xi = []
for _ in range(n):
    xi.append(int(input()))
xi.sort()
low = 1
high = xi[-1]
# 1 2 4 8 9
res = 0

def Count(distance):
    cnt = 1
    prev = xi[0]
    for x in range(1, n):
        if xi[x] - prev >= distance:
             cnt += 1
             prev = xi[x]

    return cnt


while low <= high:
    mid = (low + high) // 2

    if Count(mid) >= c:
        res = mid
        low = mid + 1
    else:
        high = mid - 1

print(res)