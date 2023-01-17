"""
nm의 길이의 네트워크 선을 1m와 2m의 길이로 자르려 한다.
"""
n = int(input())

dp = [0] * (n + 1)
dp[1] = 1
dp[2] = 2
for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[n])
#bottom up 방식

