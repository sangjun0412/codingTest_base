n = int(input())
nl = list(map(int, input().split()))
m = int(input())
nl.sort(reverse=True)
res = 21700000

def dfs(v, sum):
    global res
    if sum > m or v > res:
        return
    if sum == m:
        if v < res:
            res = v
    else:
        for i in range(n):
            dfs(v + 1, sum + nl[i])

dfs(0, 0)
print(res)