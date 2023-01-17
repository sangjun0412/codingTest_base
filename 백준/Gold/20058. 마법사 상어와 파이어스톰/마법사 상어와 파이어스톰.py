import math
from collections import deque

n, Q = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(int(math.pow(2, n)))]
graph_len = int(math.pow(2, n))
new_graph = [[0] * graph_len for _ in range(graph_len)]
visit = [[False] * graph_len for _ in range(graph_len)]



def rotate_graph(size):
    frame_size = int(math.pow(2, size))

    for x in range(0, graph_len, frame_size):
        for y in range(0, graph_len, frame_size):
            for j in range(frame_size):
                for i in range(frame_size):
                    new_graph[x + i][y + frame_size - j - 1] = graph[x + j][y + i] # 행과 열을 크로스

    for i in range(graph_len):
        for j in range(graph_len):
            graph[i][j] = new_graph[i][j]

def checking_contact_area():
    checking_area = []

    for i in range(graph_len):
        for j in range(graph_len):
            check_tmp = 0
            if new_graph[i][j] > 0:
                if 0 <= i - 1 < graph_len:
                    if new_graph[i - 1][j] > 0:
                        check_tmp += 1
                if 0 <= i + 1 < graph_len:
                    if new_graph[i + 1][j] > 0:
                        check_tmp += 1
                if 0 <= j - 1 < graph_len:
                    if new_graph[i][j - 1] > 0:
                        check_tmp += 1
                if 0 <= j + 1 < graph_len:
                    if new_graph[i][j + 1] > 0:
                        check_tmp += 1
                if check_tmp < 3:
                    checking_area.append((i,j))

    for x, y in checking_area:
        new_graph[x][y] -= 1
    for i in range(graph_len):
        for j in range(graph_len):
            graph[i][j] = new_graph[i][j]


max_area = 0

def bfs():
    global max_area
    q = deque()

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(graph_len):
        for j in range(graph_len):
            area_count = 1
            if visit[i][j] or new_graph[i][j] == 0:
                continue
            q.append((i, j))
            visit[i][j] = True
            while q:
                sx, sy = q.popleft()

                for k in range(4):
                    nx = sx + dx[k]
                    ny = sy + dy[k]
                    if nx < 0 or ny < 0 or nx >= graph_len or ny >= graph_len or visit[nx][ny]:
                        continue
                    if new_graph[nx][ny] > 0:
                        q.append((nx, ny))
                        visit[nx][ny] = True
                        area_count += 1
            max_area = max(max_area, area_count)



L = list(map(int, input().split()))
for one_L in L:
    rotate_graph(one_L)
    checking_contact_area()
bfs()



cnt = 0
for i in range(graph_len):
    for j in range(graph_len):
       cnt += new_graph[i][j]
print(cnt)
print(max_area)