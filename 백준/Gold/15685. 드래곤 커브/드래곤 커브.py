## 드래곤 커브
# 시작점, 시작 방향, 세대
# 0세대 드래곤 커브 (0,0)에서 시작 -> 시작 방향 오른쪽
# 1세대 0세대 드래곤 커브 (1,0) 끝점에서 시계방향으로 90도 회전시킨 다음 0세대 드래곤커브를 붙임
# 시작점에서 가장 먼점을 기준으로 나머지 애들을 시계방향으로 돌려버려


n = int(input())
graph = [[0] * 101 for i in range(101)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(n):
    x, y, d, g = map(int, input().split())
    graph[x][y] = 1

    direction = [d]

    for i in range(g):
        for j in range(len(direction)-1, -1, -1):
            direction.append((direction[j] + 1) % 4)

    for c in direction:
        nx = x +dx[c]
        ny = y +dy[c]
        graph[nx][ny] = 1
        x, y = nx, ny

cnt = 0

for i in range(100):
    for j in range(100):
        if graph[i][j] == 1 and graph[i+1][j] == 1  and graph[i][j+1] == 1 and graph[i +1][j +1] == 1:
            cnt += 1

print(cnt)