dp = [0] * (1001)

dp[0] = 1
dp[1] = 1

for i in range(2, 1001):
    dp[i] = dp[i - 2] * 2 + dp[i - 1]


n = int(input())
print(dp[n]%10007)