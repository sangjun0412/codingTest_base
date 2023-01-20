import heapq
n = int(input())
heap = []
for i in range(n):
    nl = list(map(int, input().split()))
    for j in nl:
        if len(heap) < n:
            heapq.heappush(heap, j)
        elif heap[0] < j:
            heapq.heappop(heap)
            heapq.heappush(heap, j)
print(heap[0])