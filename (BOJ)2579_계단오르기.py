n = int(input())
nl = list()
for i in range(n):
    nl.append(int(input()))
dp = [0] * (301)


dp[0] = 0
dp[1] = nl[0] + nl[1]
dp[2] = max(nl[1] + nl[2], nl[0] + nl[2])

for i in range(3, n ):
    dp[i] = max(dp[i - 3] + nl[i - 1] + nl[i], dp[i - 2] + nl[i])

print(dp[n - 1])