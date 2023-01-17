from collections import deque
n, m = map(int, input().split())
nl = list(map(int, input().split()))

q = deque()
for i in range(len(nl)):
    q.append((nl[i], i))
res = deque()
a, b =q[0]
while q:
    largest = max(q)
    a, b = q[0][0], q[0][1]

    if a >= largest[0]:
        res.append((q.popleft(), b))
    else:
        q.append(q.popleft())

for i in range(len(nl)):
    if res[i][1] == m:
        print(i + 1)
        break
