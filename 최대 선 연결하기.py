"""
왼쪽번호는 무조건 오름차순
오른쪽은 무작위
왼쪽 번호와 일치한 오른쪽번호와 선을 연결
서로 선이 겹치지 않고 최대 몇개의 선이 될수 있는지
이전 인덱스가 가리키는 방향보다 더 큰 방향이어야 안겹친다.
"""
n = int(list())
nl = list(map(int, input().split()))
dp = [0] * (n + 1)
dp[1] = 1
res = 0

for i in range(2, n+1):
    max = 0
    for j in range(i - 1, 0, - 1):
        if nl[j] < nl[i] and max < dp[j]:
            max = dp[j]
    dp[i] = max + 1
    if dp[i] > res:
        res = dp[i]
print(res)

