"""
노드들을 합치고, 부모를 찾아 서로소 집합을 찾는 알고리즘
트리구조를 활용
find 연산은 부모노드를 찾을때까지 재귀연산
union연산은 두 원소의 부모 노드를 찾고 번호가 큰 노드가

"""

import sys

sys.setrecursionlimit(10000000)


def find(number, parent):
    if number not in parent:
        parent[number] = number + 1
        return number
    empty = find(parent[number], parent)
    parent[number] = empty + 1
    return empty


def solution(k, room_number):
    answer = []
    parent = {}

    for i in room_number:
        ch_room = find(i, parent)
        answer.append(ch_room)
    return answer

"""
k -> 호텔의 총 방의 개수
고객이 원하는 방번호 제출 -> room_number
방이 있다면 즉시 제출. 방이 배정되어 있다면 비어있는 방 중 가장 작은 번호 방 배정.

"""
"""
k -> 호텔의 총 방의 개수
고객이 원하는 방번호 제출 -> room_number
방이 있다면 즉시 제출. 방이 배정되어 있다면 비어있는 방 중 가장 작은 번호 방 배정.

"""
# def solution(k, room_number):
#     answer = []
#     size = len(room_number)  # depth의 Max_size
#     ch = [0] * (k + 1)  # k개의 방을 체크하는 변수
#     # ch에 없다면 바로 1로 전환 및 answer에 추가.
#     # 있다면 그 다음을 확인 및 체크 반복
#
#     # 위에 방식으로 하면 효율성 테스트에서 걸린다. 그렇다면 어떻게 해결할까?
#     ch_point = list(range(1, k + 1))
#
#     def dfs(depth, ch, size):
#         if depth == size:
#             return
#         now_checking = room_number[depth]
#         while True:
#             if not ch[now_checking]:
#                 ch[now_checking] = 1
#                 tmp = now_checking
#                 answer.append(tmp)
#                 print(tmp)
#                 print(ch_point)
#                 ch_point.remove(tmp)
#                 break
#             else:
#                 now_checking = ch_point[0]  # 이 하나씩 늘리는거에서 효율성이 안좋음
#
#         dfs(depth + 1, ch, size)
#
#     dfs(0, ch, size)
#     return answer
# a= solution(10,[1,3,4,1,3,1])
# print(a)