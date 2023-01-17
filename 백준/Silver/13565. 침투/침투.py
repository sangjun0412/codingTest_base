import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [] * m

for i in range(n):
    graph.append(list(map(int, input().rstrip())))


def bfs(x, y):
    q = deque()
    q.append((x, y))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    graph[x][y] = 2
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                q.append((nx, ny))
                graph[nx][ny] = 2


for i in range(m):
    if graph[0][i] == 0:
        bfs(0, i)

if 2 in graph[-1]:
    print("YES")
else:
    print("NO")
