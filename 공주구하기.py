from collections import deque
n, k = map(int, input().split())

q = deque(list(range(1, n + 1)))

while q:
    for _ in range(k-1):
        cur = q.popleft()
        q.append(cur)
    q.popleft()
    if len(q) == 1:
        print(q[0])
        q.pop()
