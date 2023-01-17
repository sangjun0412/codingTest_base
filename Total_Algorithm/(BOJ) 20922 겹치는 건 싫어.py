n, k = map(int, input().split())
nl = list(map(int, input().split()))
start = 0
end = 0
ch = [0] * (max(nl) + 1)
answer = 0

while end < n:
    if ch[nl[end]] < k:
        ch[nl[end]] += 1
        end += 1
    else:
        ch[nl[start]] -= 1
        start += 1
    answer = max(answer, end - start)
print(answer)
