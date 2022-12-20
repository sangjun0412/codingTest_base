def compare(cdd, bd):
    for k in range(0, len(cdd)):
        x = cdd[k]
        y = bd[k]

        if len(x) != len(y):
            return 0
        else:
            for i, j in zip(x, y):
                if j == '*':
                    continue
                elif i != j:
                    return 0
    return 1


def solution(ud, bd):
    size = len(bd)
    candidate = list()
    ch = [0] * len(ud)
    res = []

    def dfs(depth, cdd, size, ud, bd, ch):
        if depth == size:
            if compare(cdd, bd):
                res.append(cdd[:])
        else:
            for i in range(0, len(ud)):
                if ch[i] == 0:
                    ch[i] = 1
                    cdd.append(ud[i])
                    dfs(depth + 1, cdd, size, ud, bd, ch)
                    cdd.pop()
                    ch[i] = 0

    dfs(0, candidate, size, ud, bd, ch)
    ans = set(''.join(sorted(x)) for x in res)
    return len(ans)