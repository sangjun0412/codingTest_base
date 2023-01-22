from collections import deque
def solution(pr, location):
    q = deque()
    for idx, x in enumerate(pr):
        q.append((x, idx))
    cnt = 0
    while True:
        max_num = max(pr)
        if q[0][0] == max_num:
            if q[0][1] == location:
                cnt += 1
                print(cnt)
                break
            else: 
                cnt += 1
                q.popleft()
                pr.remove(max_num)
        else:
            q.append(q.popleft())
    return cnt