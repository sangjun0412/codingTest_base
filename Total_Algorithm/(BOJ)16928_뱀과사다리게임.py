from collections import deque
n, m = map(int, input().split())
graph = [0] * 101
visit = [0] * 101

ladder = {}
snake = {}
for _ in range(n):
    a, b = map(int, input().split())
    ladder[a] = b

for _ in range(m):
    a, b = map(int, input().split())
    snake[a] = b

q = deque([1])
while q:
    x = q.popleft()
    if x == 100:
        print(graph[x])
        break
    for dice in range(1, 7):
        next_place = x + dice
        if next_place <= 100 and not visit[next_place]:
            if next_place in ladder.keys():
                next_place = ladder[next_place]
            if next_place in snake.keys():
                next_place = snake[next_place]
            if not visit[next_place]:
                visit[next_place] = True
                graph[next_place] = graph[x] + 1
                q.append(next_place)

