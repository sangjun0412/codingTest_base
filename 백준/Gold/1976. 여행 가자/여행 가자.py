"""
길찾기 문제 -> 다익스트라, dfs, bfs
중복이 가능함.
순서대로 가야됨 주어진 순서대로 갈 수 있는지를 체크(다 연결되어있냐 -> 주어진 도시들이)
연결되어있다 - 1 안되어있다 - 0
A-B가 연결되어 있으면, B-A도 연결 되어있다. 마지막줄에 여행계획
1부터 N까지 도시 번호
"""
from collections import deque
n = int(input()) #도시 수
m = int(input()) #여행 계획 도시 수
graph = [list(map(int, input().split())) for _ in range(n)]
nl = list(map(int, input().split()))
ch = [0 for i in range(n)]


def dfs(start):
    ch[start] = 1

    for index, j in enumerate(graph[start]):
        if j == 1 and ch[index] == 0:
            ch[index] = 1
            dfs(index)

dfs(nl[0] - 1)

if 0 not in ch:
    print("YES")
    exit()
for i in nl:
    if ch[i - 1] == 0:
        print("NO")
        exit()

print("YES")