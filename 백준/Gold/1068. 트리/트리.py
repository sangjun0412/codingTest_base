import sys
sys.setrecursionlimit(1000)


def dfs(arr, target):
    arr[target] = -2
    for i in range(len(arr)):
        if arr[i] == target:
            dfs(arr, i)


n = int(input())
nl = list(map(int, input().split()))
k = int(input())
cnt = 0

dfs(nl, k)

for j in range(len(nl)):
    if nl[j] != -2 and j not in nl:
        cnt += 1
print(cnt)