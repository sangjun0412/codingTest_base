import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))
dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])





#시간초과 왜냐 간단한 다익스트라로 해서,,
# import sys
# input = sys.stdin.readline
# INF = int(1e9)
#
# v, e = map(int, input().split())
# start = int(input())
# graph = [[] for _ in range(v + 1)]
# visited = [False] * (v + 1)
# distance = [INF] *(v + 1)
#
#
# for _ in range(e):
#     a, b, c = map(int, input().split())
#     graph[a].append((b,c))
#
#
# def get_smallest_node():
#     min_value = INF
#     index = 0
#     for i in range(1, v + 1):
#         if distance[i] < min_value and not visited[i]:
#             min_value =distance[i]
#             index = i
#     return index
#
#
# def dijkstra(start):
#     distance[start] = 0
#     visited[start] = True
#     for j in graph[start]:
#         distance[j[0]] = j[1]
#     for i in range(v - 1):
#         now = get_smallest_node()
#         visited[now] = True
#         for j in graph[now]:
#             cost = distance[now] + j[1]
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost
#
# dijkstra(start)
#
# for i in range(1, v + 1):
#     if distance[i] == INF:
#         print("INF")
#     else:
#         print(distance[i])