from collections import deque
start_x, start_y = 0, 0
end_x, end_y = 6, 6
q = deque()
q.append((start_x, start_y))
graph = [list(map(int, input().split())) for _ in range(7)]
visit = [[0] * 7 for _ in range(7)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0
while q:
    x, y = q.popleft()
    if x == end_x and y == end_y:
        print(visit[x][y])
        break
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 7 and 0 <= ny < 7:
                if graph[nx][ny] == 0:
                    q.append((nx, ny))
                    visit[nx][ny] = visit[x][y] + 1
            else:
                continue