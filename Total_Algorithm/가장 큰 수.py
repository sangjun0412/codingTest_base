n, m = map(int, input().split())
size = len(str(n))
nl = list((map(int, str(n))))

stack = []
cnt = 0
for x in nl:
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)

if m != 0:
    stack = stack[:-m]
print(*stack)