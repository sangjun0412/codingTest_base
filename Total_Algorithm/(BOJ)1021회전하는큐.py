from collections import deque
n, m = map(int, input().split())
nl = deque(list(range(1, n + 1)))
check = list(map(int, input().split()))
res = 0


for i in check:
    while True:
        if nl[0] == i:
            nl.popleft()
            break
        else:
            if nl.index(i) < len(nl) / 2:
                while nl[0] != i:
                    nl.append(nl.popleft())
                    res += 1
            else:
                while nl[0] != i:
                    nl.appendleft(nl.pop())
                    res += 1
print(res)
