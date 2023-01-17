import sys
sys.setrecursionlimit(5000)
input = sys.stdin.readline

N, M, H = map(int, input().split())

visited = [[False]* (N + 1) for i in range(H + 1)]
candidate = []

for i in range(M):
    a, b = map(int, input().split())
    visited[a][b] = True


def check():
    for i in range(1, N + 1):
        now = i
        for j in range(1, H + 1):
            if visited[j][now - 1]:
                now -= 1
            elif visited[j][now]:
                now += 1
        if now != i:
            return 0
    return 1

def dfs(depth, index):
    global result

    if depth >= result:
        return
    if check():
        result = depth
        return

    for i in range(index, len(candidate)):
        x, y = candidate[i]
        if not visited[x][y-1] and not visited[x][y + 1]:
            visited[x][y] = True
            dfs(depth + 1, i + 1)
            visited[x][y] = False

for i in range(1, H + 1):
    for j in range(1, N):
        if not visited[i][j - 1] and not visited[i][j] and not visited[i][j+1]:
            candidate.append([i,j])

result = 4
dfs(0, 0)

if result < 4:
    print(result)
else:
    print(-1)


