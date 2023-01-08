n = int(input())
nl = list(map(int, input().split()))
dp = [0] * (n + 1)
dp[0] = nl[0]
res = 0

for i in range(1, n):
    tmp = 0
    for j in range(i - 1, -1, -1):
        if nl[i] > nl[j] and dp[j] > tmp:
            tmp = dp[j]
    dp[i] = nl[i] + tmp
    if dp[i] > res:
        res = dp[i]

print(res)

