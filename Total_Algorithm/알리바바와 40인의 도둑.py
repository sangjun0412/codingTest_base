n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = graph[0][0]

for i in range(1, n):
    dp[0][i] = dp[0][n - i] + graph[0][i]
    dp[i][0] = dp[n - i][0] + graph[i][0]

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + graph[i][j]
print(dp[n- 1][n- 1])
