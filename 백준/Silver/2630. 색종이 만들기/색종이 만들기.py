import sys
input = sys.stdin.readline

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

result = []


def func(x, y, N):
    color = graph[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != graph[i][j]:
                func(x, y, N//2)
                func(x + N//2, y, N//2)
                func(x, y+N//2, N//2)
                func(x+N//2, y+N//2, N//2)
                return
    if color == 0:
        result.append(0)
    elif color == 1:
        result.append(1)


func(0, 0, N)

print(result.count(0))
print(result.count(1))
