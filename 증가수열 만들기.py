from collections import deque
n = int(input())
nl = list(map(int, input().split()))

q = deque(nl)
ans = []
res = []

while True:
    if res == []:
        if q[0] < q[-1]:
            res.append(q.popleft())
            ans.append("L")
        else:
            res.append(q.pop())
            ans.append("R")
    else:
        if res[-1] > q[0] and res[-1] > q[-1]:
            break
        if q[0] < q[-1]:
            if q[0] > res[-1]:
                res.append(q.popleft())
                ans.append("L")
            else:
                res.append(q.pop())
                ans.append("R")
        else:
            if q[-1] > res[-1]:
                res.append(q.pop())
                ans.append("R")
            else:
                res.append(q.popleft())
                ans.append("L")
print(len(ans))
for a in ans:
    print(a, end='')
