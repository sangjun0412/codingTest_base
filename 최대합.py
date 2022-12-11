from heapq import *

heap = []
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(heap) == 0:
            print(-1)
        else:
            print(heappop(heap)[1])
    else:
        heappush(heap,(-n, n))
