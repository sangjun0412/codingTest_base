N, M = map(int, input().split())
import copy

graph = []
compare_sum = 0


# 긴 막대 스타일
def long_tetro():
    global graph
    global compare_sum
    global N, M
    long_sum = 0

    for i in range(N):
        for j in range(M):
            if j + 3 < M:
                long_sum = graph[i][j] + graph[i][j + 1] + graph[i][j + 2] + graph[i][j + 3]
                if long_sum > compare_sum:
                    compare_sum = long_sum

                # 2
            if i + 3 < N:
                long_sum = graph[i][j] + graph[i + 1][j] + graph[i + 2][j] + graph[i + 3][j]
                if long_sum > compare_sum:
                    compare_sum = long_sum

    # # 가로를 이제 0~3, 1~4 이런식으로 끊어서 리스트에 전부 삽입
    # for i in graph:
    #     index = 0
    #     for no, j in enumerate(i):
    #         if no + 4 <= M:
    #             for k in range(index, index + 4):
    #                 long_sum += i[k]
    #             if index + 1 < M - 3:
    #                 index += 1
    #             if compare_sum < long_sum:
    #                 compare_sum = long_sum
    #             long_sum = 0
    # # 세로를 만들어 준 후
    # # 세로를 이제 0~3, 1~4 이런 식으로 끊어서 전부 삽입
    #
    # for i in range(M):
    #     for j in range(N):
    #         height_graph[i].append(graph[j][i])
    #
    # for i in height_graph:
    #     index = 0
    #     for no, j in enumerate(i):
    #         if no + 4 <= N:
    #             for k in range(index, index + 4):
    #                 long_sum += i[k]
    #             if index + 1 < N - 3:
    #                 index += 1
    #             if compare_sum < long_sum:
    #                 compare_sum = long_sum
    #             long_sum = 0


def square_tetro():
    global graph
    global compare_sum
    global N, M

    for i in range(N):
        for j in range(M):
            if i + 1 < N and j + 1 < M:
                square_sum = graph[i][j] + graph[i][j + 1] + graph[i + 1][j] + graph[i + 1][j + 1]

            if square_sum > compare_sum:
                compare_sum = square_sum


def L_tetro():
    global graph
    global compare_sum
    global N, M

    for i in range(N):
        for j in range(M):
            if i + 2 < N and j + 1 < M:
                l_sum = graph[i][j] + graph[i + 1][j] + graph[i + 2][j] + graph[i + 2][j + 1]
                if l_sum > compare_sum:
                    compare_sum = l_sum

            if i + 2 < N and j - 1 >= 0:
                l_sum = graph[i][j] + graph[i + 1][j] + graph[i + 2][j] + graph[i + 2][j - 1]
                if l_sum > compare_sum:
                    compare_sum = l_sum

            if i + 2 < N and j + 1 < M:
                l_sum = graph[i][j] + graph[i][j + 1] + graph[i + 1][j] + graph[i + 2][j]
                if l_sum > compare_sum:
                    compare_sum = l_sum

            if i + 2 < N and j + 1 < M:
                l_sum = graph[i][j] + graph[i][j + 1] + graph[i + 1][j + 1] + graph[i + 2][j + 1]
                if l_sum > compare_sum:
                    compare_sum = l_sum

            if i + 1 < N and j + 2 < M:
                l_sum = graph[i][j] + graph[i + 1][j] + graph[i + 1][j + 1] + graph[i + 1][j + 2]
                if l_sum > compare_sum:
                    compare_sum = l_sum

            if i + 1 < N and j - 2 >= 0:
                l_sum = graph[i][j] + graph[i + 1][j] + graph[i + 1][j - 1] + graph[i + 1][j - 2]
                if l_sum > compare_sum:
                    compare_sum = l_sum

            if i + 1 < N and j + 2 < M:
                l_sum = graph[i][j] + graph[i + 1][j] + graph[i][j + 1] + graph[i][j + 2]
                if l_sum > compare_sum:
                    compare_sum = l_sum

            if i + 1 < N and j + 2 < M:
                l_sum = graph[i][j] + graph[i][j + 1] + graph[i][j + 2] + graph[i + 1][j + 2]
                if l_sum > compare_sum:
                    compare_sum = l_sum


def thunder_tetro():
    global graph
    global compare_sum
    global N, M

    for i in range(N):
        for j in range(M):
            if i + 2 < N and j + 1 < M:
                thunder_sum = graph[i][j] + graph[i + 1][j] + graph[i + 1][j + 1] + graph[i + 2][j + 1]
                if thunder_sum > compare_sum:
                    compare_sum = thunder_sum

            if i + 2 < N and j - 1 >= 0:
                thunder_sum = graph[i][j] + graph[i + 1][j] + graph[i + 1][j - 1] + graph[i + 2][j - 1]
                if thunder_sum > compare_sum:
                    compare_sum = thunder_sum

            if i - 1 >= 0 and j + 2 < M:
                thunder_sum = graph[i][j] + graph[i][j + 1] + graph[i - 1][j + 1] + graph[i - 1][j + 2]
                if thunder_sum > compare_sum:
                    compare_sum = thunder_sum

            if i + 1 < N and j + 2 < M:
                thunder_sum = graph[i][j] + graph[i][j + 1] + graph[i + 1][j + 1] + graph[i + 1][j + 2]
                if thunder_sum > compare_sum:
                    compare_sum = thunder_sum


def oh_tetro():
    global graph
    global compare_sum
    global N, M

    for i in range(N):
        for j in range(M):
            if i - 1 >= 0 and j + 2 < M:
                oh_sum = graph[i][j] + graph[i][j + 1] + graph[i][j + 2] + graph[i - 1][j + 1]
                if oh_sum > compare_sum:
                    compare_sum = oh_sum

            # 17
            if i + 1 < N and j + 2 < M:
                oh_sum = graph[i][j] + graph[i][j + 1] + graph[i][j + 2] + graph[i + 1][j + 1]
                if oh_sum > compare_sum:
                    compare_sum = oh_sum

            # 18
            if i + 2 < N and j + 1 < M:
                oh_sum = graph[i][j] + graph[i + 1][j] + graph[i + 1][j + 1] + graph[i + 2][j]
                if oh_sum > compare_sum:
                    compare_sum = oh_sum

            # 19
            if i + 2 < N and j - 1 >= 0:
                oh_sum = graph[i][j] + graph[i + 1][j] + graph[i + 1][j - 1] + graph[i + 2][j]
                if oh_sum > compare_sum:
                    compare_sum = oh_sum


for i in range(N):
    graph.append(list(map(int, input().split())))

long_tetro()
square_tetro()
L_tetro()
thunder_tetro()
oh_tetro()

print(compare_sum)
