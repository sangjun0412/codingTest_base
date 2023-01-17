n, m = map(int, input().split())

cnt = 0
def dfs(depth):
    global cnt
    if depth == m:
        for x in a:
            print(x, end = ' ')
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):
            a.append(i)
            dfs(depth + 1)
            a.pop()


a = list()
dfs(0)
print(cnt)