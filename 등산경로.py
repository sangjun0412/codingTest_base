start = 214700000
destination = -1
start_x, start_y = 0, 0
destination_x, destination_y = 0, 0
n = int(input())
graph = []

for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    if min(tmp) < start:
        start = min(min(tmp), start)
        start_x, start_y = i, tmp.index(min(tmp))
    if max(tmp) > destination:
        destination = max(max(tmp), destination)
        destination_x, destination_y = i, tmp.index(max(tmp))

res = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
# print(start_x, start_y)
# print(destination_x, destination_y)
# visit = [[0] * n for _ in range(n)]


def dfs(x, y):

    global res
    if x == destination_x and y == destination_y:
        res += 1
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > graph[x][y]:
                    dfs(nx, ny)


dfs(start_x, start_y)
print(res)