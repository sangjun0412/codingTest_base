"""
L은 육지, W는 바다
이동은 상하좌우로만 가능
한칸 이동시 한시간
"""
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(str, input())) for _ in range(n)]
res = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, cnt):
    max1 = -1
    q = deque()
    q.append((x,y, cnt))
    visit[x][y] = 1
    while q:
        x, y, cnt =q.popleft()
        if max1 <cnt:
            max1 = cnt
        for i in range(4):
            nx = x +dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny <m and graph[nx][ny] == "L" and not visit[nx][ny]:
                 q.append((nx,ny,cnt + 1))
                 visit[nx][ny] = 1
    return max1
res = -1
for i in range(n):
    for j in range(m):
        if graph[i][j] == "L":
            visit = [[0] * m for _ in range(n)]
            res = max(res, bfs(i,j,0))
print(res)