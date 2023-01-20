n = int(input())
nl = list(map(int, input().split()))
m = int(input())
nl.sort()

start = 0
end = n - 1
cnt = 0
while start < end:
    tmp = nl[start] + nl[end]
    if tmp == m:
        cnt += 1
        start += 1
    elif tmp < m:
        start += 1
    else:
        end -= 1

print(cnt)