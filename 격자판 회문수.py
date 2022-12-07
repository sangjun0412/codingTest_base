graph = [list(map(int, input().split())) for _ in range(7)]

res = 0
# 가로 체크
for i in range(7):
    a = graph[i][0:5]
    b = graph[i][1:6]
    c = graph[i][2:7]
    tmp1 = 0
    tmp2 = 0
    tmp3 = 0
    for j in range(7//2):
        if a[j] != a[-1 -j]:
            tmp1 = 1
        if b[j] != b[-1-j]:
            tmp2 = 1
        if c[j] != c[-1-j]:
            tmp3 = 1
    if tmp1 == 0:
        res += 1
    if tmp2 ==0:
        res +=1
    if tmp3 == 0:
        res += 1

for i in range(3):
    for j in range(7):
        a = []
        for k in range(i, i + 5):
            a.append(graph[k][j])
        tmp1 = 0
        for s in range(7 // 2):
            if a[s] != a[-1-s]:
                tmp1 = 1
        if tmp1 == 0:
            res += 1

print(res)

