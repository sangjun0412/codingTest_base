n = int(input())
nl = list(map(int, input().split()))
dp = nl[:]
res = 0

for i in range(1, n):
    for j in range(i):
        if nl[i] > nl[j]:
            dp[i] = max(dp[i], dp[j] + nl[i])
print(max(dp))