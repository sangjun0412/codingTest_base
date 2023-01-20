import sys
input = sys.stdin.readline
n, k = map(int, input().split())
nl = list(map(int, input().split()))

start = 0
end = 1
res = []
res.append(sum(nl[:k]))
for i in range(n - k):
    res.append(res[i] - nl[i] + nl[k + i]) # 맨앞 빼고 맨뒤 더하고
print(max(res))