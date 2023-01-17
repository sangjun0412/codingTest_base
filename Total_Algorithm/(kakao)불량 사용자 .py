def compare(cdd, bd):
    for k in range(0, len(cdd)):
        x = cdd[k]
        y = bd[k]

        if len(x) != len(y):
            return 0
        else:
            for i, j in zip(x, y): # candidate와 ban 리스트 비교
                if j == '*':
                    continue
                elif i != j:
                    return 0
    return 1 # 끝까지 가면 Okay


def solution(ud, bd):
    size = len(bd)
    candidate = list()
    ch = [0] * len(ud)
    res = []

    def dfs(depth, cdd, size, ud, bd, ch): # cdd candidate, ud -> user_id , bd -> banned_id, ch -> 중복순열이 아닌 순열로
        if depth == size:
            if compare(cdd, bd):
                res.append(cdd[:]) # cdd로 하면, 얕은 복사가 되서, 원치 않는 값으로 마지막 복사가 됨.
        else:
            for i in range(0, len(ud)):
                if ch[i] == 0:
                    ch[i] = 1
                    cdd.append(ud[i])
                    dfs(depth + 1, cdd, size, ud, bd, ch)
                    cdd.pop()
                    ch[i] = 0

    dfs(0, candidate, size, ud, bd, ch)
    ans = set(''.join(sorted(x)) for x in res) # 정렬 후, set으로 중복되는 candidate 삭제
    return len(ans)