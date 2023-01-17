from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

visited = [False]*(n+1)


def bfs(n):
    q = deque([n])
    visited[n] = True
    while q:
        target = q.popleft()
        for i in graph[target]:
            if not visited[i]:
                visited[i] = visited[target] + 1
                q.append(i)


res = []
for i in range(1, n):
    visited = [False] * (n + 1)
    bfs(i)
    res.append(sum(visited))

print(res.index(min(res)) + 1)
