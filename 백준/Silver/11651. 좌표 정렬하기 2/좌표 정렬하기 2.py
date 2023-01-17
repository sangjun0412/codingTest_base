n = int(input())
array = []

for _ in range(n):
    n, m = map(int, input().split())
    array.append([m, n])

sort_array = sorted(array)
for y, x in sort_array:
    print(x, y)
