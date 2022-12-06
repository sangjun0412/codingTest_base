n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse= True)
b = list()
for i in range(n):
    for j in range(i + 1, n):
        for m in range(j + 1, n):
            tmp = a[i] + a[j] + a[m]
            b.append(tmp)

print(b[k-1])