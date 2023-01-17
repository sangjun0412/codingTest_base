"""
귤의 리스트가 있고, k개의 귤을 골랐을때 최소 종류가 되는 방법.
딕셔너리에 담고 value값이 높은 순으로 고른다. 끝
"""


def solution(k, tangerine):
    answer = 0
    dic = {}
    check = [0] * (10000001)
    for x in tangerine:
        if not check[x]:
            check[x] = 1
            dic[x] = 1
        else:
            dic[x] += 1
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    for key, v in dic:
        answer += 1
        k -= v
        if k <= 0:
            break

    return answer