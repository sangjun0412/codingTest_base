
def solution(s):
    answer = True
    stack = []    
    for x in s:
        if stack ==[]:
            if x == ')':
                return False
            stack.append(x)
        elif stack[-1] == '(':
            if x == '(':
                stack.append(x)
            elif x == ')':
                stack.pop()

    if stack != []:
        return False
    
    return True