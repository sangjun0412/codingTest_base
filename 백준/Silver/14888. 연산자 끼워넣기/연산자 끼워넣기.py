N = int(input())
A_list = list(map(int, input().split()))
cal_list = list(map(int, input().split()))
max_value = -10000000000
min_value = 10000000000

def dfs(idx,total, p,m,ml,d):
    global max_value, min_value
    if idx == N:
        max_value = max(total, max_value)
        min_value = min(total, min_value)
    if p:
        dfs(idx + 1, total + A_list[idx], p - 1, m, ml, d)
    if m:
        dfs(idx + 1, total - A_list[idx], p, m - 1, ml, d)
    if ml:
        dfs(idx + 1, total * A_list[idx], p, m, ml - 1, d)
    if d:
        dfs(idx + 1, int(total / A_list[idx]), p, m, ml, d - 1)


dfs(1, A_list[0], cal_list[0], cal_list[1], cal_list[2], cal_list[3])
print(max_value)
print(min_value)