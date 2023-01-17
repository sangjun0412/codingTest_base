n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
res = []

def dfs(x, y):
    global cnt
    cnt += 1
    graph[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny]:
            dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt = 0
            dfs(i, j)
            res.append(cnt)
print(len(res))
res.sort()
for x in res:
    print(x)