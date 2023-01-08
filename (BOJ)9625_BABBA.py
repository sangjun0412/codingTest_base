"""
화면이 처음에는 A
A -> B
B -> BA
A와 B의 개수는?
"""
n = int(input())
dp = [[0] * (n + 1) for _ in range(2)]
# x = 0 -> A, x = 1 - > B
dp[0][0] = 1
dp[1][1] = 1

for i in range(2, n + 1):
    dp[0][i] = dp[0][i - 1] + dp[0][i - 2]
    dp[1][i] = dp[1][i - 1] + dp[1][i - 2]

print(dp[0][n], dp[1][n])