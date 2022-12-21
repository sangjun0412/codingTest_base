n, m = map(int, input().split())
nl = list(range(1, n + 1))
res = [0] * m
cnt = 0


def dfs(depth, s):
    global cnt
    if depth == m:
        for j in range(depth):
            print(res[j], end=' ')
        print()
        cnt +=1
        return
    else:
        for i in range(s, n + 1):
            res[depth] = i
            dfs(depth+1, i + 1)

dfs(0, 1)
print(cnt)