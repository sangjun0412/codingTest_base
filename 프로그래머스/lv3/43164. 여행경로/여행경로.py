from collections import deque
def solution(tickets):
    answer = []
    q = deque()
    q.append(("ICN", ["ICN"], []))
    
    while q:
        airport, path, used = q.popleft()
        
        if len(used) == len(tickets):
            answer.append(path)
            
        for i in range(len(tickets)):
            if tickets[i][0] == airport and not i in used:
                q.append((tickets[i][1], path + [tickets[i][1]], used + [i]))
    answer.sort()
        
    return answer[0]