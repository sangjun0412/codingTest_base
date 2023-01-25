import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    nl = list()
    nl2 = list()
    for i in range(n):
        a, b = map(int, input().split())
        nl.append((a, b))
    nl.sort()
    top = 0
    result = 1

    for i in range(1, len(nl)):
        if nl[i][1] < nl[top][1]:
            top = i
            result += 1
    print(result)
