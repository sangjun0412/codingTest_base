"""
학자에게 n개의 대학에서 강연요청을 해왔다.
d일안에서 와서 강연을 해주면 p만큼의 강연료
각대학에서의 d와 p값은 서로 다를수도 있음
가장 많은 돈
하루 최대 한곳에서만 가능
"""
import heapq

n = int(input())
schedule = []
heap = []
for i in range(n):
    p, d = map(int, input().split())
    schedule.append((p, d))
schedule = sorted(schedule, key=lambda x:x[1])
for x in schedule:
    heapq.heappush(heap, x[0])
    if len(heap) > x[1]:
        heapq.heappop(heap)
print(sum(heap))