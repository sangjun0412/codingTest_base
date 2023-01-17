import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x = []
y = []
for _ in range(n):
    x.append(str(input()))
for _ in range(m):
    y.append(str(input()))

result = list(set(x) & set(y))
result.sort()

print(len(result))
print(''.join(result), end = '')
