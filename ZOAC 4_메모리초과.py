"""
거리두기 수칙을 지켜야함
한 명씩 앉을 수 있는 테이블이 행마다 W개씩 H행에 걸쳐있다
세로로 n칸 또는 가로로 m칸 이상 비우고 앉아야 함.
최대 몇명 수용이 가능한지
"""
from collections import deque

h, w, n, m = map(int, input().split())
graph = [[0] * w for i in range(h)] # 공간 설정
q = deque()
q.append((0,0))

dx = [0, n + 1]
dy = [m + 1, 0]

cnt = 0

while q:
    x, y = q.popleft()
    if not graph[x][y]:
        graph[x][y] = 1
        cnt += 1
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < h and ny < w:
                q.append((nx, ny))

print(cnt)
