import math


def solution(n, a, b):
    answer = 1
    ##1 2 3 4 5 6 7 8
    # 1 3 5 7
    # 4 7
    a, b = a - 1, b - 1
    while True:
        if a // 2 == b // 2:
            return answer
        else:
            a = a // 2
            b = b // 2
            answer += 1
