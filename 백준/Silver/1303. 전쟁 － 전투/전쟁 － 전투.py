"""
내 병사는 W
상대 병사는 B
뭉쳐있으면 n**2
"""
from collections import deque
n, m = map(int, input().split())
graph = [list(map(str, input())) for _ in range(m)]
visit = [[0] * n for _ in range(m)]
me = 0
rival = 0


def bfs(x,y):
    global sum_w
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visit[nx][ny] and graph[nx][ny] == "W":
                sum_w.append(1)
                visit[nx][ny] = 1
                q.append((nx, ny))

def bfs2(x,y):
    global sum_b
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visit[nx][ny] and graph[nx][ny] == "B":
                sum_b.append(1)
                visit[nx][ny] = 1
                q.append((nx, ny))

for i in range(m):
    for j in range(n):
        if not visit[i][j] and graph[i][j] =="W":
            sum_w = [1]
            visit[i][j] = 1
            bfs(i,j)
            me += (len(sum_w) ** 2)
visit = [[0] * n for _ in range(m)]

for i in range(m):
    for j in range(n):
        if not visit[i][j] and graph[i][j] =="B":
            sum_b = [1]
            visit[i][j] = 1
            bfs2(i, j)
            rival += (len(sum_b) ** 2)
print(me, rival)