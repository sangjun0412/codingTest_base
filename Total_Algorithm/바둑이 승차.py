c, n = map(int, input().split())
nl = []
for _ in range(n):
    nl.append(int(input()))


maximum = 0


def dfs(v, total, tsum):
    global maximum
    if total + (ttotal - tsum) < maximum:
            return
    if total > c:
        return
    if v == n:
        if maximum < total:
            maximum = total
        return
    else:
        dfs(v + 1, total + nl[v], tsum + nl[v])
        dfs(v + 1, total, tsum + nl[v])

ttotal = sum(nl)
dfs(0, 0, 0)
print(maximum)