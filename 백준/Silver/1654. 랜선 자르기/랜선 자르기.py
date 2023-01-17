import sys

k, n = map(int, input().split())
x = []

for i in range(k):
    x.append(int(input()))

x.sort()
start = 1
end = x[-1]

while(start <= end):
    mid = (start + end) // 2
    cnt = 0
    for i in x:
        cnt += i//mid
    if cnt >= n:
        start = mid +1
    else:
        end = mid - 1
print(end)