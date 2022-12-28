from collections import deque
move = [1, -1, 5]
s, e = map(int, input().split())
q = deque()
q.append(s)
visit = [0] * (100000)
dis = [0] *(100000)

visit[s] = 1
dis[s] = 0
q = deque()
q.append(s)
while q:
    x = q.popleft()
    if x == e:
        break
    for next in (x - 1, x + 1, x + 5):
        if 0 < next < 10000:
            if visit[next] == 0:
                q.append(next)
                visit[next] = 1
                dis[next] = dis[x] + 1
print(dis[e])