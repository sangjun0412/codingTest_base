t = int(input())
k = int(input())
nl = list()
pl = list()
for i in range(k):
    p, n = map(int, input().split())
    pl.append(p)
    nl.append(n)


ans = 0
def dfs(depth, res):
    global ans
    if res > t: #edge cutting이 제대로 안되서 타임아웃 됬었음
        return
    if depth == k:
        if res == t:
            ans += 1
        return
    else:
        for i in range(0, nl[depth] + 1):
            dfs(depth + 1, res + pl[depth] * i)

dfs(0, 0)
print(ans)