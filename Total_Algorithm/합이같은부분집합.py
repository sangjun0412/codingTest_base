import sys
n = int(input())
nl = list(map(int, input().split()))
ch = [0] * (n + 1)

res = []

def dfs(v, sum):
    if v == n:
        if sum == (total - sum):
            print("YES")
            sys.exit(0)
        else:
            dfs(v + 1, sum + nl[v])
            dfs(v + 1, sum)

total = sum(nl)
dfs(0,0)
print("NO")