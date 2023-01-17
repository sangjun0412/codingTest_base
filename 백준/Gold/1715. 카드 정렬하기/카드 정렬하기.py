import heapq

n = int(input())
heap = []
for i in range(n):
    heapq.heappush(heap, int(input()))
result = []
while heap:
    if len(heap) == 1:
        break
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    third = first + second
    result.append(third)
    heapq.heappush(heap, third)

res = 0
for x in result:
    res += x
print(res)


