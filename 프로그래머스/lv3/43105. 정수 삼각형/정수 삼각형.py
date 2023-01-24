def solution(triangle):
    answer = 0
    
    if len(triangle) == 1:
        return (''.join(triangle[0]))
        
    dp = []
    for i in range(1, len(triangle) + 1):
        dp.append([0] * i)
    for i in range(len(triangle)):
        if i == 0:
            dp[i][0] = triangle[i][0]
            dp[i][-1] = triangle[i][-1]
        else:
            dp[i][0] = triangle[i][0] + dp[i - 1][0]
            dp[i][-1] = triangle[i][-1] + dp[i - 1][-1]
    if len(triangle) == 2:
        print(max(dp[1]))
        return
    else:
        for i in range(2, len(triangle)):
            for j in range(1, i):
                dp[i][j] = triangle[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j])

    return (max(dp[len(triangle) - 1]))