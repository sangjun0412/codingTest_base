n, k = map(int, input().split())
nl = list(map(int, input().split()))
for _ in range(k):
    s, e = map(int, input().split())
    s = s - 1
    tmp = 0
    for i in range(s, e):
        tmp += nl[i]
    res = '{:.2f}'.format(round(tmp/(e - s), 2))
    print(res)
