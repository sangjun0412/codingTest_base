from collections import deque
n, m = map(int, input().split())

rl = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    rl[a].append(b)
    rl[b].append(a)

res = 0

def dfs(depth, next):
    global res
    visit[next] = 1
    if depth == 4:
        res = 1
        return

    for i in rl[next]:
        if not visit[i]:
            visit[i] = 1
            dfs(depth + 1, i)
            visit[i] = 0

for i in range(n):
    visit = [0] * 2001
    dfs(0, i)
    if res == 1:
        break

print(res)