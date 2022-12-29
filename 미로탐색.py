graph = [list(map(int, input().split())) for _ in range(7)]

res = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visit = [[0] * 7 for _ in range(7)]

def dfs(x, y):
    global res
    visit[x][y] = 1
    if x == 6 and y == 6:
        res += 1
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 7 and 0 <= ny < 7:
                if graph[nx][ny] == 0 and visit[nx][ny] == 0:
                    visit[nx][ny] = 1
                    dfs(nx, ny)
                    visit[nx][ny] = 0

dfs(0, 0)
print(res)