"""
중간값 정하는건 -> 결국 최대힙 최소힙이 길이가 같을때,
최소힙의 가장 TOP값이 정답,,
"""

import heapq,sys
input = sys.stdin.readline
n = int(input())

A = []
B = []

for i in range(n):
    x = int(input())
    if len(A) == len(B):
        heapq.heappush(A, -x)
    else:
        heapq.heappush(B, x)
    if not B: # 최소힙이 비어있다면
        print(-A[0])
        continue
    if -A[0] > B[0]:
        n = - heapq.heappop(A)
        m = heapq.heappop(B)
        heapq.heappush(A, -m)
        heapq.heappush(B, n)
    print(-A[0])