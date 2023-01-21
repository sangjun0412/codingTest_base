from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

n, k = map(int, input().split())
distance = [INF] * (100001)

distance[n] = 0


def bfs():
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()
        for i in range(3):
            if i == 0:
                nx = x + 1
            elif i == 1:
                nx = x - 1
            else:
                nx = x * 2
            if 0 <= nx < 100001 and nx == x * 2:
                if distance[x] < distance[nx]:
                    distance[nx] = distance[x]
                    q.append(nx)
            elif 0 <= nx < 100001:
                if distance[x] + 1 < distance[nx]:
                    distance[nx] = distance[x] + 1
                    q.append(nx)

bfs()

print(distance[k])