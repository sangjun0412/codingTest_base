"""
2*n 타일링
dp
범위가 적을경우 전부다 미리 dp 테이블을 설정하여야 한다!
"""
n = int(input())

dp = [0] *(1002)

dp[1] = 1
dp[2] = 2
for i in range(3, 1001):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n]%10007)
