def solution(s):
    answer = ''
    s =s.lower()
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
        else:
            if s[i - 1] == ' ' or i == 0:
                answer += s[i].upper()
            else:
                answer += s[i]
    return answer