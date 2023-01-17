"""
세로 r칸 가로 c칸
dfs or bfs 인데 체크를
처음에 한거는 이게 bfs인데 dfs느낌으로 해야 됨
예제 3에서 너비 탐색을 할 시, 바로 멈추는 문제가 있음
그래서 queue를 set형식으로 하고 z부분에 점점 추가하는 형식으로 해야됨!!!
"""
import sys

R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
answer = 1


def BFS(x, y):
    global answer
    q = set([(x, y, board[x][y])])
    while q:
        x, y, ans = q.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ((0 <= nx < R) and (0 <= ny < C)) and (board[nx][ny] not in ans):
                q.add((nx,ny,ans + board[nx][ny]))
                answer = max(answer, len(ans)+1)

BFS(0, 0)
print(answer)



# """
# 세로 r칸 가로 c칸
# dfs or bfs 인데 체크를
# """
# from collections import deque
# r, c = map(int, input().split())
# graph = []
# for i in range(r):
#     tmp = list(map(str, input()))
#     graph.append(tmp)
# check = set()
# for i in range(r):
#     for j in range(c):
#         check.add(graph[i][j])
# dic = {}
# for x in check:
#     dic[x] = 0
#
# visit = [[0] * c for _ in range(r)]
# q = deque()
# q.append((0,0))
# dx = [0,0,1,-1]
# dy = [1,-1,0,0]
# cnt = 0
# dic[graph[0][0]] = 1
# while q:
#     x, y = q.popleft()
#     visit[x][y] = 1
#     cnt += 1
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < r and 0 <= ny < c:
#             if not visit[nx][ny] and dic[graph[nx][ny]] == 0:
#                 q.append((nx, ny))
#                 visit[nx][ny] = 1
#                 dic[graph[nx][ny]] = 1
# print(cnt)
