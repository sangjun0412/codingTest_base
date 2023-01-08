n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[n - 1][n - 1] = graph[n - 1][n - 1]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    if dp[x][y] > 0:
        return dp[x][y]
    if x == 0 and y == 0:
        return graph[0][0]
    else:
        if y == 0:
            dp[x][y] = dfs(x - 1, y) + graph[x][y]
            return
        elif x == 0:
            dp[x][y] = dfs(x, y - 1) + graph[x][y]
        else:
            dp[x][y] = min(dfs(x - 1, y), dfs(x, y - 1)) + graph[x][y]
        return dp[x][y]


print(dfs(n - 1, n - 1))
