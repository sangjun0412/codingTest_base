from collections import deque
n = int(input())
res = deque()


def cal(n):
    if n == 1:
        res.appendleft(1)
        return
    if n % 2 == 1:
        res.appendleft(1)
        cal(n // 2)
    elif n % 2 == 0:
        res.appendleft(0)
        cal(n // 2)

cal(n)
for i in range(len(res)):
    print(res[i], end = '')
