import heapq


def solution(operations):
    max_heap = []
    min_heap = []
    heapq.heapify(max_heap)
    heapq.heapify(min_heap)

    for x in operations:
        op, num = map(str, x.split(" "))
        num = int(num)
        if op == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        elif op == 'D' and num == 1:
            if len(max_heap) == 0:
                continue
            tmp = -heapq.heappop(max_heap)
            min_heap.remove(tmp)
        elif op == 'D' and num == -1:
            if len(max_heap) == 0:
                continue
            tmp = heapq.heappop(min_heap)
            max_heap.remove(-tmp)

    if len(max_heap) == 0:
        answer = [0, 0]
    else:
        answer = [max(min_heap), min(min_heap)]

    return answer