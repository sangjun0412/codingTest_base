import sys
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = set()
for i in range(n):
    for j in range(i + 1, n):
        for m in range(j + 1, n):
            b.add(a[i] + a[j] + a[m])
c = list(b)
c.sort(reverse=True)
print(c[k-1])