def solution(s):
    s = list(map(int, s.split()))
    a = str(min(s))
    b = str(max(s))
    answer = a + " " + b

    return answer