"""
야근피로도 야근을 시작한 시점에서 남은일의 작업량 제곱하여 전부 다 더한 값
N시간동안 일할 수 있고 최소화 시켜야함.
최대값을 계속해서 갱신하기 때문에 최대힙~
"""
import heapq
def solution(n, works):
    answer = 0
    heap = []
    if sum(works) < n:
        return 0
    
    for x in works:
        heapq.heappush(heap,-x)
    
    while n > 0:
        tmp = -heapq.heappop(heap)
        tmp -= 1
        heapq.heappush(heap, -tmp)
        n -= 1
    
    for x in heap:
        answer += x ** 2
    
    return answer
    
