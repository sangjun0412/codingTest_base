from collections import deque
def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        q = deque(skill)
        flag = 0
        for sk in tree:
            if sk not in q:
                continue
            else:
                if sk == q[0]:
                    q.popleft()
                else:
                    flag = 1
                    break
        if flag == 0:
            answer+= 1
    return answer