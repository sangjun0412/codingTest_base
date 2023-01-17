import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nl = list(map(int, input().split()))
check = [0]
tmp = 0
for x in nl:
    tmp += x
    check.append(tmp)

for i in range(m):
    a, b = map(int,input().split())
    print(check[b] - check[a - 1])
