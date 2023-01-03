"""
1,1부터 시작하는 nXn크기의 땅
각각의 칸은 r,c로 표현
처음 양분은 모두 5만큼씩 들어있다.

봄 - 자신의 나이만큼 양분을 먹는다. 나이가 한살 증가, 각각의 나무는 나무가 있는 1칸의 양분만 먹을 수 있다. 하나의 칸에 여러개의 나무가 있다면
나이가 어린 나무부터 양분을 먹는다. 만약, 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.
여름 - 죽은 나무가 양분으로 변함. 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분 추가, 소수점 아래는 버린다.
가을 - 나무가 번식 번식하는 나무의 나이가 5의 배수이어야 하며, 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
겨울 - s2d2가 땅을 돌아다니면서 양분을 추가. 각칸에 추가되는 양분의 양은 A[r][c]이고 입력으로 주이진다.
K년이 지난 후 상도의 땅에 살아있는 나무의 개수 출력

"""
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, 1, -1, -1]

n, m, k = map(int, input().split())
plus_a = [list(map(int, input().split())) for _ in range(n)]
a = [[5]*n for _ in range(n)]
tree = [[[] for _ in range(n)] for _ in range(n)] # 처음에 할때는 이중배열로 해서 그런듯 삼중배열로 해야 파이파이 통과

for _ in range(m):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)

for year in range(k):

    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                tree[i][j].sort()
                temp_tree, dead_tree = [], 0
                for age in tree[i][j]:
                    if age <= a[i][j]:
                        a[i][j] -= age
                        age += 1
                        temp_tree.append(age)
                    else:
                        dead_tree += age // 2
                a[i][j] += dead_tree
                tree[i][j] = []
                tree[i][j].extend(temp_tree)

    if not tree:
        print(0)
        sys.exit()

    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                for age in tree[i][j]:
                    if age % 5 == 0:
                        for dir in range(8):
                            ni = i + dx[dir]
                            nj = j + dy[dir]
                            if 0 <= ni < n and 0 <= nj < n:
                                tree[ni][nj].append(1)

    for i in range(n):
        for j in range(n):
            a[i][j] += plus_a[i][j]

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(tree[i][j])
print(ans)

#
# import sys, copy
# from collections import deque
#
# input = sys.stdin.readline
#
# # 양분 그래프 n x n , m나무개수, k년이 지난 후
# n, m, k = map(int, input().split())
# # 나무 양분 그래프
# plus_soil = []
# for _ in range(n):
#     plus_soil.append(list(map(int, input().split())))
#
# origin_soil = [[5] * n for _ in range(n)]
# # 나중에 겨울에 양분 추가해줄 그래프  = plus_soil
#
# # 살아있는 나무 그래프
# live = []
# for _ in range(m):
#     x, y, z = map(int, input().split())
#     live.append((x - 1, y - 1, z))
#
# # 봄에 나이가 어린 나무 부터 양분을 먹게하기위한 정렬
#
#
# # live = [] # 살아있는 나무들 리스트를 알아야 가을에 번식을 할 수 있다.
# for _ in range(k):
#     live.sort(key=lambda x: (x[0], x[1], x[2]))
#     death = []  # 양분못먹어서 죽은 나무들의 좌표를 넣어두는 리스트
#     spring_q = deque(live)
#     # 봄
#     while spring_q:
#         tree_x, tree_y, tree_age = spring_q.popleft()
#         # 양분 먹을 때
#         if origin_soil[tree_x][tree_y] >= tree_age:
#             origin_soil[tree_x][tree_y] -= tree_age
#             live.remove((tree_x, tree_y, tree_age))
#             live.append((tree_x, tree_y, tree_age + 1))
#             # 양분 못먹을 떄
#         else:
#             death.append((tree_x, tree_y, tree_age))
#             live.remove((tree_x, tree_y, tree_age))
#
#     # 여름
#     summer_q = deque(death)
#     while summer_q:
#         death_x, death_y, death_age = summer_q.popleft()
#         origin_soil[death_x][death_y] += death_age // 2
#
#     # 가을
#     dx = [-1, -1, 0, 1, 1, 1, 0, -1]
#     dy = [0, 1, 1, 1, 0, -1, -1, -1]
#
#     fall_q = deque(live)
#     # print("fall_q",fall_q)
#
#     while fall_q:
#         live_x, live_y, live_age = fall_q.popleft()
#         if live_age % 5 == 0:
#             for i in range(8):
#                 nx = live_x + dx[i]
#                 ny = live_y + dy[i]
#                 if 0 <= nx < n and 0 <= ny < n:
#                     live.append((nx, ny, 1))
#     # 겨울
#     for i in range(n):
#         for j in range(n):
#             origin_soil[i][j] += plus_soil[i][j]
#
# print(len(live))