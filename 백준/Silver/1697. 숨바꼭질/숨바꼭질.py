import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    q = deque([n])

    while q:
        v = q.popleft()
        if v == k:
            print(dist[v])
            break

        for nx in (v - 1, v + 1, v * 2):
            if 0 <= nx <= max and not dist[nx]:
                dist[nx] = dist[v] + 1
                q.append(nx)


max = 10 ** 5
dist = [0] * (max + 1)
n, k = map(int, input().split())

bfs()
