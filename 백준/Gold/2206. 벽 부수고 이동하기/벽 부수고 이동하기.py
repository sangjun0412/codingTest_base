"""
n*m 행렬의 그래프
맵에서 0 은 이동할 수 있는 곳
1은 이동할 수 없는
(1,1)에서 시작 (n,m)의 위치로 가려하는 최단경로
단 하나의 벽을 부술 수 있다.
최단거리를 출력, 불가능할 시 -1
상하좌우로만 이동가능
"""
from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visit = [[[0] * 2 for i in range(m)] for i in range(n)]
visit[0][0][1] = 1

q = deque()
q.append((0, 0, 1))


def bfs():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0 ,0]

    while q:
        x, y, z = q.popleft()
        if (x, y) == (n - 1, m - 1):
            return visit[x][y][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and z == 1:
                    visit[nx][ny][0] = visit[x][y][1] + 1
                    q.append((nx, ny, 0))
                elif graph[nx][ny] == 0 and visit[nx][ny][z] == 0:
                    visit[nx][ny][z] = visit[x][y][z] + 1
                    q.append((nx, ny, z))
    return -1

print(bfs())