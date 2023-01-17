import sys
input = sys.stdin.readline

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

res = []


def func(x, y, N):
    color = graph[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != graph[i][j]:
                n = N//3
                n2 = N*2//3
                func(x, y, n)
                func(x, y + n, n)
                func(x, y + n2, n)
                func(x+n, y, n)
                func(x+n, y+n, n)
                func(x+n, y+n2, n)
                func(x+n2, y, n)
                func(x+n2, y+n, n)
                func(x+n2, y+n2, n)
                return
    if color == -1:
        res.append(-1)
    elif color == 1:
        res.append(1)
    elif color == 0:
        res.append(0)


func(0, 0, N)

print(res.count(-1))
print(res.count(0))
print(res.count(1))
