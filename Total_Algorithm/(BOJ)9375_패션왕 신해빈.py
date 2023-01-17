tc = int(input())
for t in range(tc):
    dic = {}
    n = int(input())
    for i in range(n):
        name, kind = map(str, input().split())
        if kind in dic.keys():
            dic[kind] += 1
        else:
            dic[kind] = 1
    answer = 1
    for x, v in dic.items():
        answer *= (v + 1)
    print(answer -1 )