n = int(input())
nl = list(range(1, n))
visit = [0] * (n + 1)

def dfs(v):
    if v == n + 1:
        for i in range(1, n + 1):
            if visit[i] == 1:
                print(i, end = ' ')
        print()
    else:
        visit[v] = 1
        dfs(v + 1)
        visit[v] = 0
        dfs(v + 1)


dfs(1)