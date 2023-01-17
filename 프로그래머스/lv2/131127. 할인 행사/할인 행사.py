import copy
def solution(want, number, discount):
    answer = 0
    user = []
    for a, b in zip(want, number):
        for i in range(b):
            user.append(a)
    user.sort()
    
    for i in range(0, len(discount) - 9):
        tmp = discount[i:i+10]
        tmp.sort()
        if user == tmp:
            answer += 1
        

            
    return answer