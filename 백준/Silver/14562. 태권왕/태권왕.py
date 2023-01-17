from collections import deque
import sys
input = sys.stdin.readline
c = int(input())


def bfs(x, y):
    q = deque()
    q.append((x, y, 0))
    visited = [0] * 200
    while q:
        nx, ny, cnt = q.popleft()
        if nx <= ny and visited[nx] == 0:
            q.append((nx + nx, ny + 3, cnt + 1))
            q.append((nx + 1, ny, cnt + 1))
            if nx == ny:
                return cnt


for _ in range(c):
    a, b = map(int, input().split())
    print(bfs(a, b))
