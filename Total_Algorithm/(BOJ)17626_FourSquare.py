n = int(input())
dp = [0] * (n + 1)
dp[0] = 0
dp[1] = 1
for i in range(2, n + 1):
    min_val = 217400000
    j = 1
    while (j ** 2) <= i:
        min_val = min(min_val,dp[i-(j**2)])
        j += 1
    dp[i] = min_val + 1
print(dp[n])