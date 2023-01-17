from collections import deque

t = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(graph, x, y):
    que = deque()
    que.append((x, y))
    graph[x][y] = 0

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                que.append((nx, ny))
    return


for i in range(t):
    cnt = 0
    n, m, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                cnt += 1
    print(cnt)
