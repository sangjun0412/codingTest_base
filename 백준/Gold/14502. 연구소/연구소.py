n, m = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]
tmp = [[0] * m for i in range(n)]
answer = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                dfs(nx, ny)


def select(cnt):
    global answer
    answer_tmp = 0
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                tmp[i][j] = graph[i][j]
        for i in range(n):
            for j in range(m):
                if tmp[i][j] == 2:
                    dfs(i, j)
        for i in range(n):
            answer_tmp += int(tmp[i].count(0))
        answer = max(answer, answer_tmp)
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                cnt += 1
                select(cnt)
                graph[i][j] = 0
                cnt -= 1


select(0)
print(answer)
