n = int(input())
nl = [int(input()) for _ in range(n)]
dp = [0] *(n)

if len(nl)<=2:
    print(sum(nl))
else:
    dp[0] = nl[0]
    dp[1] = nl[0] + nl[1]
    for i in range(2, n):
        dp[i] = max(dp[i - 3] +nl[i - 1] + nl[i],dp[i-2] + nl[i])
    print(dp[-1])