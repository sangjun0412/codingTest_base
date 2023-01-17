n = int(input())
table = []
for _ in range(n):
    s, e = map(int, input().split())
    table.append((s,e))

table.sort(key=lambda x : (x[1], x[0]))

endpoint = 0
cnt = 0
for t in table:
    start, end = t[0], t[1]
    if endpoint <= start:
        cnt += 1
        endpoint =end
print(cnt)