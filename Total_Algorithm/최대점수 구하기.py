n, limit = map(int, input().split())
nl = list()

for i in range(n):
    score, time = map(int, input().split())
    nl.append((score, time))
ms = -214700000 # max score


def dfs(depth, tt, ss): # tt -> total time, ss -> score sum
    global ms
    if tt > limit:
        return
    if depth == n:
        if ms < ss:
            ms = ss
        return
    else:
        dfs(depth + 1, tt+nl[depth][1], ss+nl[depth][0])
        dfs(depth + 1, tt, ss)


dfs(0, 0, 0)
print(ms)