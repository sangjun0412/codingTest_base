"""
일직선위에 n개의 높이의 서로 다른 탑을 수평 직선의 왼쪽부터 오른쪽 방향으로 세운다.
각 탑의 꼭대기에 레이저 송신기 설치
6 9 5 7 4
"""
from collections import deque
n = int(input())
tower = list(map(int, input().split()))

stack = []
answer = []
for i in range(n):
    while stack:
        if stack[-1][0] > tower[i]:
            answer.append(stack[-1][1] + 1)
            break
        else:
            stack.pop()
    if not stack:
        answer.append(0)
    stack.append([tower[i], i])
print(*answer)
#time out
# start = len(tower)
# end = len(tower) - 1
#
# while start > 0:
#     if tower[start - 1] < tower[end - 1]:
#         answer.appendleft(end)
#         start -= 1
#         end = start - 1
#     else:
#         if end == 0:
#             answer.appendleft(0)
#             start -= 1
#             end = start -1
#         else:
#             end -= 1
#
# print(*answer)