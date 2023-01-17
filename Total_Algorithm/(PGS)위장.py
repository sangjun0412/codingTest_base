def solution(clothes):
    answer = 1
    dic = {}
    for y, x in clothes:
        if x not in dic:
            dic[x] = 1
        else:
            dic[x] += 1

    for k, v in dic.items():
        answer *= (v + 1)
    return answer - 1