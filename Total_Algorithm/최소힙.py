from heapq import *
heap = []

while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        print(heappop(heap))
    else:
        heappush(heap, n)
