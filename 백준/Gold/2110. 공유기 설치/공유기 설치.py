import sys

n, m = map(int, sys.stdin.readline().split())
list1 = []
for i in range(n):
    list1.append(int(sys.stdin.readline()))
list1.sort()

start = 1
end = list1[n-1] - list1[0]

result = []

while (start <= end):
    mid = (start + end) // 2
    count = 1
    current = list1[0]
    for x in list1:
        if current + mid <= x:
            count += 1
            current = x
    if count >= m:
        start = mid + 1
        result.append(mid)
    else:
        end = mid - 1

print(max(result))
