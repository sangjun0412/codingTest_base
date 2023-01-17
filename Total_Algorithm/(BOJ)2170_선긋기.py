"""
주어지는 두위치가 10억이니까
포문을 돌리면 안됨

"""
n = int(input())
nl = list()
for i in range(n):
    start, end = map(int, input().split())
    nl.append((start, end))
nl.sort()
start = nl[0][0]
end = nl[0][1]
ans = 0
for i in range(1, n):
    ns, ne = nl[i]
    if end > ns:
        end = max(end, ne)
    else:
        ans += (end - start)
        start, end = ns, ne

ans += (end - start)
print(ans)