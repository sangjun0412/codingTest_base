import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

q = deque()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append((i, j))


def bfs():
    nx = [1, -1, 0, 0]
    ny = [0, 0, 1, -1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]
            if 0 <= dx < N and 0 <= dy < M and graph[dx][dy] == 0:
                graph[dx][dy] = graph[x][y] + 1
                q.append((dx, dy))


bfs()

res = 0

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res - 1)
