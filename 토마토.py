from collections import deque
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
q = deque()
wall = []
res =1
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))

while q:
    cnt += 1
    x, y = q.popleft()
    for i in range(4):
        nx = x +dx[i]
        ny = y +dy[i]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx, ny))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            exit()
    res = max(res, max(graph[i]))
print(res - 1)