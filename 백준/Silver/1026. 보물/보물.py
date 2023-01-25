n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)
res = 0
for x, y in zip(a,b):
    res += x*y
print(res)