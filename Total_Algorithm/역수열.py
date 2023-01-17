n = int(input())
nl = list(map(int, input().split()))
res = [0] * (n)

for i, x in enumerate(nl):
    cnt = 0
    pos = 0
    i = i + 1
    for ch in res: # 들어갈 장소 찾기
        if cnt == x:
            if res[pos] != 0:
                pos += 1
        if cnt == x and res[pos] == 0:
            break
        if ch > i:
            cnt += 1
            pos += 1
        elif ch == 0:
            cnt += 1
            pos += 1
        else:
            pos += 1
    res[pos] = i
for s in res:
    print(s, end = ' ')

# print(res)



