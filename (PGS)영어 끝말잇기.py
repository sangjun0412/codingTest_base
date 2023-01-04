import math


def solution(n, words):
    dic = {}  # 한번들어왔는지 체크
    ch = []  # 이어지는지 체크
    for i in range(len(words)):
        if words[i] not in dic:
            dic[words[i]] = 1
        else:
            if (i + 1) % n == 0:
                return [n, math.ceil((i + 1) / n)]
            else:
                return [(i + 1) % n, math.ceil((i + 1) / n)]

    for i in range(len(words)):
        if ch == []:
            ch.append(words[i][-1])
        else:
            if ch[-1] == words[i][0]:
                ch.pop()
                ch.append(words[i][-1])
            else:

                if (i + 1) % n == 0:
                    return [n, math.ceil((i + 1) / n)]
                else:
                    return [(i + 1) % n, math.ceil((i + 1) / n)]
    return [0, 0]