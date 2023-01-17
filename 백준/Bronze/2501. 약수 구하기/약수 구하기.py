n, k = map(int, input().split())
check = []

for i in range(1 , n//2 + 1):
    if n % i == 0:
        check.append(i)
check.append(n)

if len(check) < k:
    print(0)
else:
    print(check[k - 1])
