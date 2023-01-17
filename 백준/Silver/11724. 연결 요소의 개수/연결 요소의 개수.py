import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

visited = [False] * (n + 1)


def bfs(n):
    q = deque([n])
    visited[n] = True
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


cnt = 0

for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)
