from math import factorial

n, k = map(int, input().split())
a = factorial(n)
b = factorial(k)
c = factorial(n-k)
d = a/(b*c)
print(int(d))
