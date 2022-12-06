testcase = int(input())
for tc in range(testcase):
    n, s, e, k = map(int, input().split())
    nlist = list(map(int, input().split()))
    newllist = nlist[s - 1:e]
    newllist.sort()
    print(f'#{tc + 1} {newllist[k - 1]}')