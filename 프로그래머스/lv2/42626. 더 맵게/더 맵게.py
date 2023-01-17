import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while True:
        if scoville[0] >= K:
            break
        elif scoville[0] < K and len(scoville) < 2:
            answer = -1
            break
        else:
            a= heapq.heappop(scoville)
            b= heapq.heappop(scoville)
            tmp = a + b * 2
            heapq.heappush(scoville, tmp)
        answer += 1
    return answer