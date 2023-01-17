import sys
input = sys.stdin.readline

N = int(input())

graph = [list(map(int, input().rstrip())) for _ in range(N)]


def func(x, y, N):
    color = graph[x][y]
    for i in range(x, x+N):
        for j in range(y, y + N):
            if color != graph[i][j]:
                color = -1

    if color == -1:
        print("(", end='')
        func(x, y, N//2)
        func(x, y + N//2, N//2)
        func(x + N//2, y, N//2)
        func(x + N//2, y+N//2, N//2)
        print(")", end='')
    elif color == 1:
        print(1, end="")
    elif color == 0:
        print(0, end="")


func(0, 0, N)
