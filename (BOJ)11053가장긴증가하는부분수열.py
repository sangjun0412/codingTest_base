n = int(input())
nl = list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(n):
    for j in range(i):
        if nl[i] > nl[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))