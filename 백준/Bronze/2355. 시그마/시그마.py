n, m = map(int, input().split())
if n > m:
    m, n = n, m

print(int(m * (m + 1) // 2 - n*(n - 1) // 2))