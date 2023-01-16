import sys
input = sys.stdin.readline
from collections import deque

w, n = map(int, input().split())
jw = deque()
for i in range(n):
    m, p = map(int, input().split())
    jw.append((m, p))

j = sorted(jw, key=lambda x:x[1],reverse=True)
point = 0
answer = 0

while w >= 0 and point < n:
    if w - j[point][0] >= 0:
        answer += j[point][0] * j[point][1]
        w -= j[point][0]
    else:
        answer += w * j[point][1]
        w = 0
    point += 1
print(answer)
