"""
삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0 이상 9999 이하이다.
-> 삼각형의 크기가 1부터니까 dp 테이블 설정시 주의!


"""

n = int(input())
nl = []
for _ in range(n):
    nl.append(list(map(int, input().split())))

if n == 1:
    print(*nl[0])
    exit()


dp = []
for i in range(1, n + 1):
    dp.append([0] * i)

for i in range(n):
    if i == 0:
        dp[i][0] = nl[i][0]
        dp[i][-1] = nl[i][-1]
    else:
        dp[i][0] = nl[i][0] + dp[i - 1][0]
        dp[i][-1] = nl[i][-1] + dp[i - 1][-1]

if n == 2:
    print(max(dp[1]))
    exit()
else:
    for i in range(2, n):
        for j in range(1, i):
            dp[i][j] = nl[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j])
print(max(dp[n - 1]))

