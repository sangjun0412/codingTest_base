import sys
sys.setrecursionlimit(30000)

input = sys.stdin.readline

n = int(input())
x, y = map(int, input().split())  # 출발지, 목적지
m = int(input())

graph = [[] for i in range(n + 1)]  # 가족 관계

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

visited = [0] * (n+1)


def dfs(x):
    for i in graph[x]:
        if visited[i] == 0:
            visited[i] = visited[x] + 1
            dfs(i)


dfs(x)

if visited[y] == 0:
    print(-1)
else:
    print(visited[y])
