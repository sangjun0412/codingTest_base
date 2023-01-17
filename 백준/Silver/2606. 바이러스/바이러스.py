from collections import deque

n = int(input())
m = int(input())
graph = [[] for i in range(n+1)]
visit = []


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(x):
    que = deque([x])
    visit.append(x)

    while que:
        v = que.popleft()
        for i in graph[v]:
            if i not in visit:
                que.append(i)
                visit.append(i)


bfs(1)
print(len(visit)-1)
