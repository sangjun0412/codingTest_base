tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    nl = list(map(int, input().split()))
    dic = {}
    for x in nl:
        if x not in dic:
            dic[x] = 1
        else:
            dic[x] += 1
    dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)
    print(f'#{t} {dic[0][0]}')