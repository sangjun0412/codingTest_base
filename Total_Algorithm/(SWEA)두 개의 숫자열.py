tc = int(input())

for t in range(1, tc+1):
    n, m = map(int, input().split())
    nl = list(map(int, input().split()))
    ml = list(map(int, input().split()))
    if n > m:
        n, m = m, n
        nl, ml = ml, nl
    max_sum = 0
    for i in range(m - n + 1):
        tmp = 0
        for j in range(n):
            tmp += nl[j] * ml[i + j]
        if max_sum < tmp:
            max_sum =tmp
    print(f'#{t} {max_sum}')

