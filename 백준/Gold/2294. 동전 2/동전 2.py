n, k =map(int, input().split())
nl = []
dp = [10001] * (k + 1)
dp[0] = 0
for i in range(n):
    nl.append(int(input()))
for x in nl:
    for j in range(x, k + 1):
        dp[j] = min(dp[j], dp[j-x] + 1)
if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])
