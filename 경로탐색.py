n, m = map(int, input().split())
graph = [[0] * (n + 1) for i in range(n + 1)]
ch = [0]*(n + 1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
cnt = 0
ch[1] = 1


def dfs(v):
    global cnt
    if v == n:
        cnt += 1
    else:
        for i in range(1, n + 1):
            if graph[v][i] == 1 and ch[i] == 0:
                ch[i] = 1
                dfs(i)
                ch[i] = 0

dfs(1)
print(cnt)