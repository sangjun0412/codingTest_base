n, m = map(int, input().split())
cnt = 0


def dfs(depth):
    global cnt
    if depth == m:
        for i in a:
            print(i, end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                a.append(i)
                dfs(depth + 1)
                a.pop()
                ch[i]= 0
ch = [0] *(n + 1)
a = list()
dfs(0)
print(cnt)