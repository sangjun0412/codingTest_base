"""
오늘부터 n+1일째 되는 날 휴가를 가기 위해, 남은 n일 동안 최대한 많은 상담
각각의 상담은 완료하는데 날수 T와 금액 P로 이루어져있음
n일 동안 최대수익이 나도록 구하라
"""

n = int(input())
a = []
res = 0
for i in range(n):
    t, p = map(int, input().split())
    a.append((t, p))


def dfs(depth, p):
    global res
    if depth > n:
        return
    if depth == n:
        if res < p:
            res = p
        return
    else:
        dfs(depth + a[depth][0], p + a[depth][1])
        dfs(depth + 1, p)

dfs(0, 0)
print(res)