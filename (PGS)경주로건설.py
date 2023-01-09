"""
0은칸이 비어있고 1은 벽이다.
(0,0) 출발 -> (n-1, n-1) 도착
상하좌우로 인접한 두빈칸을 연결하여 건설.
상하 또는 좌우로 이어지면 직선도로
직각으로 만나는 지점 코너
직선도로는 하나만들면 100원
코너는 500원
최소비용을 계산해야함
"""
from collections import deque


def bfs(board, dir):
    size = len(board)
    dp = [[214700000] * size for _ in range(size)]
    q = deque()
    q.append((0, 0, 0, dir))
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while q:
        x, y, c, z = q.popleft()
        if x == size - 1 and y == size - 1:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = i
            if 0 > nx or nx >= size or 0 > ny or ny >= size:
                continue
            if board[nx][ny] == 1:
                continue
            if z == nz:
                nc = c + 100
            else:
                nc = c + 600
            if dp[nx][ny] > nc:
                dp[nx][ny] = nc
                q.append((nx, ny, nc, nz))
    return dp[-1][-1]


def solution(board):
    answer = min(bfs(board, 0), bfs(board, 2))
    return answer

