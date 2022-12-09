n, m = map(int, input().split())

nl = list(map(int, input().split()))

nl.sort(reverse=True)
cnt = 0

while nl:
    if len(nl) == 1:
        nl.pop()
        cnt += 1
    if nl == []:
        break
    if nl[0] + nl[-1] > m:
        nl.pop(0)
        cnt += 1
    elif nl[0] + nl[-1] <= m:
        nl.pop(0)
        nl.pop()
        cnt += 1


print(cnt)