n, k = map(int, input().split())
dp = [0] * (k + 1)
nl =[]
dp[0] = 1
for i in range(n):
    nl.append(int(input()))
for x in nl:
    for j in range(x, k + 1):
        if j - x >= 0:
            dp[j] += dp[j - x]
print(dp[k])
