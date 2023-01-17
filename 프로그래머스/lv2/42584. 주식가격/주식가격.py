from collections import deque
def solution(prices):
    answer = []
    q = deque(prices)
    while q:
        x =q.popleft()
        time = 0
        for i in q:
            time += 1
            if x > i:
                break
            
                
        answer.append(time)
    return answer