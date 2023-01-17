n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
total = 0
for i in range(n):
    for j in range(n):
        total += graph[i][j]


def sand(x, y, idx):
    if graph[x][y] > 0 and idx == 0: #
        # 모래 빼주는 비율 옮겨야 하는 양
        sand_seven_x = [1, -1]
        sand_seven_y = [0, 0]
        sand_ten_x = [1, -1]
        sand_ten_y = [-1, - 1]
        sand_one_x = [-1, 1]
        sand_one_y = [1, 1]
        sand_five_x = [0]
        sand_five_y = [-2]
        sand_two_x = [2, -2]
        sand_two_y = [0, 0]
        ## 모래 이동 좌표
        sand_tmp_seven = int(graph[x][y] * 0.07)
        sand_tmp_ten = int(graph[x][y] * 0.1)
        sand_tmp_one = int(graph[x][y] * 0.01)
        sand_tmp_five = int(graph[x][y] * 0.05)
        sand_tmp_two = int(graph[x][y] * 0.02)
        if sand_tmp_seven > 0:
            graph[x][y] -= sand_tmp_seven * 2 # sandseven 빼주기
            for i in range(2): #sandseven을 좌표에 찍고 없으면 안찍음
                if 0 <= x + sand_seven_x[i] < n and 0 <= y + sand_seven_y[i] < n:
                    graph[x + sand_seven_x[i]][y + sand_seven_y[i]] += sand_tmp_seven
        if sand_tmp_ten > 0:
            graph[x][y] -= sand_tmp_ten * 2 #sandten
            for i in range(2):
                if 0 <= x + sand_ten_x[i] < n and 0 <= y + sand_ten_y[i] < n:
                    graph[x + sand_ten_x[i]][y + sand_ten_y[i]] += sand_tmp_ten
        if sand_tmp_two > 0:
            graph[x][y] -= sand_tmp_two * 2#samdtwo
            for i in range(2):
                if 0 <= x + sand_two_x[i] < n and 0 <= y + sand_two_y[i] < n:
                    graph[x + sand_two_x[i]][y + sand_two_y[i]] += sand_tmp_two
        if sand_tmp_one > 0:
            graph[x][y] -= sand_tmp_one * 2
            for i in range(2):
                if 0 <= x + sand_one_x[i] < n and 0 <= y + sand_one_y[i] < n:
                    graph[x + sand_one_x[i]][y + sand_one_y[i]] += sand_tmp_one
        if sand_tmp_five > 0:
            graph[x][y] -= sand_tmp_five
            if 0 <= x + sand_five_x[0] < n and 0 <= y + sand_five_y[0] < n:
                graph[x + sand_five_x[0]][y + sand_five_y[0]] += sand_tmp_five
        if graph[x][y] > 0:
            alpha = graph[x][y]
            graph[x][y] = 0
            if 0 <= x < n and 0 <= y - 1 < n:
                graph[x][y - 1] += alpha
    if graph[x][y] > 0 and idx == 1: #아래로 갈때

        # 모래 빼주는 비율 옮겨야 하는 양
        sand_seven_x = [0, 0]
        sand_seven_y = [1, -1]
        sand_ten_x = [1, 1]
        sand_ten_y = [-1, 1]
        sand_one_x = [-1, -1]
        sand_one_y = [-1, 1]
        sand_five_x = [2]
        sand_five_y = [0]
        sand_two_x = [0, 0]
        sand_two_y = [2, -2]
        ## 모래 이동 좌표
        sand_tmp_seven = int(graph[x][y] * 0.07)
        sand_tmp_ten = int(graph[x][y] * 0.1)
        sand_tmp_one = int(graph[x][y] * 0.01)
        sand_tmp_five = int(graph[x][y] * 0.05)
        sand_tmp_two = int(graph[x][y] * 0.02)
        if sand_tmp_seven > 0:
            graph[x][y] -= sand_tmp_seven * 2  # sandseven 빼주기
            for i in range(2):  # sandseven을 좌표에 찍고 없으면 안찍음
                if 0 <= x + sand_seven_x[i] < n and 0 <= y + sand_seven_y[i] < n:
                    graph[x + sand_seven_x[i]][y + sand_seven_y[i]] += sand_tmp_seven
        if sand_tmp_ten > 0:
            graph[x][y] -= sand_tmp_ten * 2  # sandten
            for i in range(2):
                if 0 <= x + sand_ten_x[i] < n and 0 <= y + sand_ten_y[i] < n:
                    graph[x + sand_ten_x[i]][y + sand_ten_y[i]] += sand_tmp_ten
        if sand_tmp_two > 0:
            graph[x][y] -= sand_tmp_two * 2  # samdtwo
            for i in range(2):
                if 0 <= x + sand_two_x[i] < n and 0 <= y + sand_two_y[i] < n:
                    graph[x + sand_two_x[i]][y + sand_two_y[i]] += sand_tmp_two
        if sand_tmp_one > 0:
            graph[x][y] -= sand_tmp_one * 2
            for i in range(2):
                if 0 <= x + sand_one_x[i] < n and 0 <= y + sand_one_y[i] < n:
                    graph[x + sand_one_x[i]][y + sand_one_y[i]] += sand_tmp_one
        if sand_tmp_five > 0:
            graph[x][y] -= sand_tmp_five
            if 0 <= x + sand_five_x[0] < n and 0 <= y + sand_five_y[0] < n:
                graph[x + sand_five_x[0]][y + sand_five_y[0]] += sand_tmp_five
        if graph[x][y] > 0:
            alpha = graph[x][y]
            graph[x][y] = 0
            if 0 <= x + 1 < n and 0 <= y < n:
                graph[x + 1][y] += alpha
    if graph[x][y] > 0 and idx == 3: # 위로 올라갈때

        # 모래 빼주는 비율 옮겨야 하는 양
        sand_seven_x = [0, 0]
        sand_seven_y = [-1, 1]
        sand_ten_x = [-1, -1]
        sand_ten_y = [-1,  1]
        sand_one_x = [1, 1]
        sand_one_y = [-1, 1]
        sand_five_x = [-2]
        sand_five_y = [0]
        sand_two_x = [0, 0]
        sand_two_y = [2, -2]
        ## 모래 이동 좌표
        sand_tmp_seven = int(graph[x][y] * 0.07)
        sand_tmp_ten = int(graph[x][y] * 0.1)
        sand_tmp_one = int(graph[x][y] * 0.01)
        sand_tmp_five = int(graph[x][y] * 0.05)
        sand_tmp_two = int(graph[x][y] * 0.02)
        if sand_tmp_seven > 0:
            graph[x][y] -= sand_tmp_seven * 2 # sandseven 빼주기
            for i in range(2): #sandseven을 좌표에 찍고 없으면 안찍음
                if 0 <= x + sand_seven_x[i] < n and 0 <= y + sand_seven_y[i] < n:
                    graph[x + sand_seven_x[i]][y + sand_seven_y[i]] += sand_tmp_seven
        if sand_tmp_ten > 0:
            graph[x][y] -= sand_tmp_ten * 2 #sandten
            for i in range(2):
                if 0 <= x + sand_ten_x[i] < n and 0 <= y + sand_ten_y[i] < n:
                    graph[x + sand_ten_x[i]][y + sand_ten_y[i]] += sand_tmp_ten

        if sand_tmp_two > 0:
            graph[x][y] -= sand_tmp_two * 2#samdtwo
            for i in range(2):
                if 0 <= x + sand_two_x[i] < n and 0 <= y + sand_two_y[i] < n:
                    graph[x + sand_two_x[i]][y + sand_two_y[i]] += sand_tmp_two
        if sand_tmp_one > 0:
            graph[x][y] -= sand_tmp_one * 2
            for i in range(2):
                if 0 <= x + sand_one_x[i] < n and 0 <= y + sand_one_y[i] < n:
                    graph[x + sand_one_x[i]][y + sand_one_y[i]] += sand_tmp_one
        if sand_tmp_five > 0:
            graph[x][y] -= sand_tmp_five
            if 0 <= x + sand_five_x[0] < n and 0 <= y + sand_five_y[0] < n:
                graph[x + sand_five_x[0]][y + sand_five_y[0]] += sand_tmp_five
        if graph[x][y] > 0:
            alpha = graph[x][y]
            graph[x][y] = 0
            if 0 <= x - 1 < n and 0 <= y < n:
                graph[x - 1][y] += alpha
    if graph[x][y] > 0 and idx == 2: #오른쪽

        # 모래 빼주는 비율 옮겨야 하는 양
        sand_seven_x = [1, -1]
        sand_seven_y = [0, 0]
        sand_ten_x = [1, -1]
        sand_ten_y = [1, 1]
        sand_one_x = [1, -1]
        sand_one_y = [-1, -1]
        sand_five_x = [0]
        sand_five_y = [2]
        sand_two_x = [2, -2]
        sand_two_y = [0, 0]
        ## 모래 이동 좌표
        sand_tmp_seven = int(graph[x][y] * 0.07)
        sand_tmp_ten = int(graph[x][y] * 0.1)
        sand_tmp_one = int(graph[x][y] * 0.01)
        sand_tmp_five = int(graph[x][y] * 0.05)
        sand_tmp_two = int(graph[x][y] * 0.02)
        if sand_tmp_seven > 0:
            graph[x][y] -= sand_tmp_seven * 2  # sandseven 빼주기
            for i in range(2):  # sandseven을 좌표에 찍고 없으면 안찍음
                if 0 <= x + sand_seven_x[i] < n and 0 <= y + sand_seven_y[i] < n:
                    graph[x + sand_seven_x[i]][y + sand_seven_y[i]] += sand_tmp_seven
        if sand_tmp_ten > 0:
            graph[x][y] -= sand_tmp_ten * 2  # sandten
            for i in range(2):
                if 0 <= x + sand_ten_x[i] < n and 0 <= y + sand_ten_y[i] < n:
                    graph[x + sand_ten_x[i]][y + sand_ten_y[i]] += sand_tmp_ten
        if sand_tmp_two > 0:
            graph[x][y] -= sand_tmp_two * 2  # samdtwo
            for i in range(2):
                if 0 <= x + sand_two_x[i] < n and 0 <= y + sand_two_y[i] < n:
                    graph[x + sand_two_x[i]][y + sand_two_y[i]] += sand_tmp_two
        if sand_tmp_one > 0:
            graph[x][y] -= sand_tmp_one * 2
            for i in range(2):
                if 0 <= x + sand_one_x[i] < n and 0 <= y + sand_one_y[i] < n:
                    graph[x + sand_one_x[i]][y + sand_one_y[i]] += sand_tmp_one
        if sand_tmp_five > 0:
            graph[x][y] -= sand_tmp_five
            if 0 <= x + sand_five_x[0] < n and 0 <= y + sand_five_y[0] < n:
                graph[x + sand_five_x[0]][y + sand_five_y[0]] += sand_tmp_five
        if graph[x][y] > 0:
            alpha = graph[x][y]
            graph[x][y] = 0
            if 0 <= x < n and 0 <= y + 1 < n:
                graph[x][y + 1] += alpha


def make_tornado(n):
    dx = [0, 1, 0, -1] # 좌 아래 우 위
    dy = [-1, 0, 1, 0]
    start_x = int(n // 2)
    start_y = int(n // 2)
    time = 0
    while True:
        for i in range(4):
            if i == 2 or i == 0:
                time = time + 1
            for j in range(1, time + 1):
                start_x, start_y = start_x + dx[i], start_y + dy[i]
                sand(start_x, start_y, i)
                # for k in range(n):
                #     for l in range(n):
                #         print(graph[k][l], end = ' ')
                #     print()
                # print()
                if start_x == 0 and start_y == 0:
                    return



make_tornado(n)


rest = 0
for i in range(n):
    for j in range(n):
        rest += graph[i][j]

print(total - rest)