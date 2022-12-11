from collections import deque

n = int(input())
nl = deque()
tmp = deque()
for i in range(n):
    nl.append(input())

for i in range(n-1):
    tmp.append(input())

while nl:
    if nl[0] in tmp:
        nl.popleft()
    else:
        print(nl[0])
        break