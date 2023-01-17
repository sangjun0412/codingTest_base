"""
적록색약 -> 빨초 같게
아닌 사람 다르게
bfs or dfs
"""
from collections import deque
n = int(input())
graph = [list(map(str,input())) for _ in range(n)]
visit = [[0] * n for _ in range(n)]


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        now_color  = graph[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and not visit[nx][ny]:
                if graph[nx][ny] == now_color:
                    q.append((nx,ny))
                    visit[nx][ny] = 1


three_color = 0
for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            bfs(i, j)
            three_color += 1

visit = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == "R":
            graph[i][j] ="G"
second_color = 0

for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            bfs(i, j)
            second_color += 1
print(three_color,second_color)