def solution(s):
    answer = -1
    s = list(map(str, s))
    stack = []
    for x in s:
        if stack == []:
            stack.append(x)
        else:
            if stack[-1] == x:
                stack.pop()
            else:
                stack.append(x)
    
    if stack == []:
        return 1
    else:
        return 0
    