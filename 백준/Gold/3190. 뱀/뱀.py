from collections import deque

n = int(input())
k = int(input())
graph = [[0] * n for _ in range(n)]

for i in range(k):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 2 # 사과 위치


l = int(input())
dic = dict()

for i in range(l):
    x, c = input().split()
    dic[int(x)] = c # 돌아야되는 구간


x, y = 0, 0
graph[0][0] = 1
answer = 0
direction = 0

def turn(c):
    global direction

    if c == "L":
        direction = (direction - 1) % 4

    else:
        direction = (direction + 1) % 4


q = deque()
q.append((x, y))
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# 맨처음 오른쪽 이제

while True:
    answer += 1

    x += dx[direction]
    y += dy[direction]

    if 0 > x or y < 0 or x >= n or y >= n:
        break

    if graph[x][y] == 2:
        graph[x][y] = 1
        q.append((x, y))
        if answer in dic:
            turn(dic[answer])
    elif graph[x][y] == 0:
        graph[x][y] = 1
        q.append((x, y))
        tx, ty = q.popleft()
        graph[tx][ty] = 0
        if answer in dic:
            turn(dic[answer])
    else:
        break

print(answer)