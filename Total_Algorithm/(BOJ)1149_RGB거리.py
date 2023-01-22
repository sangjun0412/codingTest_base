import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]
dp[0][0] = graph[0][0]
dp[0][1] = graph[0][1]
dp[0][2] = graph[0][2]

for i in range(1, n):
    dp[i][0] = min(dp[i - 1][1], dp[i- 1][2]) + graph[i][0]
    dp[i][1] = min(dp[i - 1][2], dp[i- 1][0]) + graph[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i- 1][1]) + graph[i][2]
print(min(dp[n - 1]))





# nl = []
# res = int(1e9)
# previous =0
#
# def dfs(depth, cnt, previous):
#     global res
#     if cnt > res:
#         return
#     if depth == n:
#         if res > cnt:
#             res = cnt
#             return
#     else:
#         for i in range(3):
#             if i == previous:
#                 continue
#             else:
#                 dfs(depth + 1, cnt + nl[depth][i], i)
#
#
# for i in range(n):
#     a, b, c = map(int, input().split())
#     nl.append((a,b,c))
#
# dfs(0, 0, -1)
# print(res)
