from collections import deque
n, m = map(int, input().split()) #세로, 가로

graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

ans = []


def bfs():
    q = deque()
    q.append([0,0])
    visit[0][0] = 1
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny <m and not visit[nx][ny]:
                if graph[nx][ny] == 0:
                    visit[nx][ny] = 1
                    q.append((nx,ny))
                elif graph[nx][ny] == 1:
                    visit[nx][ny] = 1
                    graph[nx][ny] = 0
                    cnt += 1
    ans.append(cnt)
    return cnt
time = 0
while True:
    time += 1
    visit = [[0] * m for _ in range(n)]
    cnt = bfs()
    if cnt == 0:
        break
print(time - 1)
print(ans[-2])
