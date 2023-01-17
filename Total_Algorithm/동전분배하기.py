n = int(input())
nl = list()
for i in range(n):
    nl.append(int(input()))
answer = [0] * 3
res = 217400000


def dfs(depth):
    global res
    if depth == n:
        cha = max(answer) - min(answer)
        if res > cha:
            tmp = set()
            for x in answer:
                tmp.add(x)
            if len(tmp) == 3:
                res = cha
        return
    else:
        for i in range(3):
            answer[i] += nl[depth]
            dfs(depth + 1)
            answer[i] -= nl[depth]

dfs(0)
print(res)