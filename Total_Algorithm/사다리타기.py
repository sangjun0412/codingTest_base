graph = [list(map(int, input().split())) for _ in range(10)]

for i in range(10):
    if graph[9][i] == 2:
        start_x, start_y = 9, i
        break
ch = [[0] * 10 for _ in range(10)]


def dfs(x, y):
    ch[x][y] = 1
    if x == 0:
        print(y)
        return
    else:
        if y - 1 >= 0 and graph[x][y - 1] == 1 and ch[x][y - 1] == 0:
            dfs(x, y -1)
        elif y + 1 < 10 and graph[x][y + 1] == 1 and ch[x][y + 1] == 0:
            dfs(x, y + 1)
        else:
            dfs(x-1, y)
dfs(start_x,start_y)