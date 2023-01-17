"""
1은 집이 있는 곳
0은 집이 없는 곳
bfs or dfs 둘다 하면 될듯
단지의 개수를 정하고 단지에 속한 집의 개수를 오름차순으로 출력
"""
from collections import deque
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
q = deque()

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
res = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            graph[i][j] = 0
            cnt = 1
            q.append((i, j))
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny]:
                        graph[nx][ny] = 0
                        cnt += 1
                        q.append((nx, ny))
            res.append(cnt)
print(len(res))
res.sort()
for x in res:
    print(x)