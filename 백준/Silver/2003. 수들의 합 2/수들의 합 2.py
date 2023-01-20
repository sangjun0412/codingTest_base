n, m = map(int, input().split())
nl = list(map(int,input().split()))

start = 0
end = 1
count = 0
while end <= n and start <= end:
    if sum(nl[start:end]) == m:
        end += 1
        count += 1
    elif sum(nl[start:end]) < m:
        end += 1
    else:
        start += 1
print(count)