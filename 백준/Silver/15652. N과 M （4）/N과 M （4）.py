N, M = map(int, input().split())
answer = []

def dfs(idx):
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    for i in range(idx, N + 1):
        answer.append(i)
        dfs(i)
        answer.pop()

dfs(1)