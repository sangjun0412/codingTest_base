from collections import deque
n = int(input())
q = deque()
while True:
    packet = int(input())
    if packet == -1:
        break
    if packet == 0:
        q.popleft()
    else:  
        q.append(packet)

if len(q) == 0:
    print("empty")
else:
    print(*q)