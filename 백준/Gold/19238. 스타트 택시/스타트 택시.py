from collections import deque

N, M, fuel = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

start_x, start_y = map(int, input().split())
start_x -= 1
start_y -= 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

people = []
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    # 각 사람의 출발위치, 도착위치를 받음.
    people.append([[x1, y1], [x2, y2]])

time = 0
no = 0

# print(people)

while time < M:
    # 현재 시점을 기준으로 가장 가까운 사람이 누구인지 받기
    # 모든 사람한테 구하면 시간초과가 난다. 가장 가까운 사람만 찾게 길찾기로 BFS구하기
    q = deque()
    q.append([start_x, start_y])
    temp = [[-1] * N for _ in range(N)]
    temp[start_x][start_y] = 0
    min_dis = 1e9
    while q:
        n_x, n_y = q.popleft()
        for d in range(4):
            nx = n_x + dx[d]
            ny = n_y + dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 1:
                continue
            if temp[nx][ny] >= 0:
                continue
            temp[nx][ny] = temp[n_x][n_y] + 1
            q.append([nx, ny])
    move = []
    # print(temp)
    for i in range(len(people)):
        p_x, p_y = people[i][0]
        now_dis = temp[p_x][p_y]
        if now_dis < 0:
            continue
        if min_dis > now_dis:
            min_dis = now_dis
            move.clear()
            move.append([p_x, p_y, now_dis, i])
        elif min_dis == now_dis:
            move.append([p_x, p_y, now_dis, i])

    move.sort()
    # move가 없는 경우도 실패로 본다
    if len(move) == 0:
        no = 1
        break

    # 가장 가까운 사람한테로 ㄱㄱ+도착지점 받기
    move_x, move_y, use_fuel, pop_people = move.pop(0)
    # print(move_x,move_y)
    # 현자 남은 연료로 이동할 수 있다면
    if fuel - use_fuel > 0:
        fuel -= use_fuel
        start_x = move_x
        start_y = move_y
    # 이동이 불가능하다면 break
    else:
        no = 1
        break
    # print(use_fuel)
    # 이제 도착지점으로 이동한다
    # 승객을 태웠다는 개념으로, 도착받자마자 해당 사람 리스트에서 뺴기
    final_x, final_y = people[pop_people][1]
    people.pop(pop_people)
    # 도착거리까지 최단경로 구하기

    temp = [[-1] * N for _ in range(N)]
    q = deque()
    q.append([start_x, start_y])
    temp[start_x][start_y] = 0
    while q:
        n_x, n_y = q.popleft()
        for d in range(4):
            nx = n_x + dx[d]
            ny = n_y + dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 1:
                continue
            if temp[nx][ny] > 0:
                continue
            temp[nx][ny] = temp[n_x][n_y] + 1
            q.append([nx, ny])

    now_dis = temp[final_x][final_y]
    # 도착까지 기름이 되는지 판단
    if now_dis < 0:
        no = 1
        break

    if fuel - now_dis >= 0:
        fuel -= now_dis
        start_x = final_x
        start_y = final_y
    else:
        no = 1
        break
    # 도착했다면, 이동하는 동안  소모한 기름 *2를 채워줌
    fuel += now_dis * 2
    time += 1
    if time == M:
        no = 0
        break
    # print(use_fuel)
    # print(now_dis)
    # print(fuel)
if no == 1:
    print(-1)
else:
    print(fuel)