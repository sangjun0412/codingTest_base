import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

n = int(input().rstrip())

graph = list(map(int, input().split()))

start = int(input().rstrip())

visited = [0] * (n)

cnt = 1


def dfs(x):
    global cnt
    for nx in (x + graph[x], x - graph[x]):
        if 0 <= nx < n and visited[nx] == 0:
            visited[nx] = 1
            cnt += 1
            dfs(nx)


dfs(start - 1)


print(cnt)
