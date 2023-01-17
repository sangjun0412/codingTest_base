n, m = map(int, input().split())

r, c, d = map(int, input().split())

graph = [list(map(int, input().split())) for i in range(n)]

visit = [[0] * m for i in range(n)]

visit[r][c] = 1

clean_cnt = 1

# 북 동 서 남
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn():
    global d
    d -= 1
    if d == -1:
        d = 3


turn_cnt = 0
while True:
    turn()

    nx = r + dx[d]
    ny = c + dy[d]

    if graph[nx][ny] == 0 and visit[nx][ny] == 0:
        visit[nx][ny] = 1
        r = nx
        c = ny
        clean_cnt += 1
        turn_cnt = 0
        continue
    else:
        turn_cnt += 1

    if turn_cnt == 4:
        nx = r - dx[d]
        ny = c - dy[d]
        if graph[nx][ny] == 0:
            r = nx
            c = ny
        else:
            break
        turn_cnt = 0

print(clean_cnt)
