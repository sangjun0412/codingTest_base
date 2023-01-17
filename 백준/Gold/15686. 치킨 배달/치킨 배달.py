from itertools import combinations

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []


def calculate(x1, y1, x2, y2):
    return int(abs(x1 - x2) + abs(y1 - y2))


def solve(num_list):
    global answer
    tmp = 0
    for i in chicken_distance:
        for j in i:
            if j[1] in num_list:
                tmp += j[0]
                break
        if tmp >= answer:
            return
    answer = min(answer, tmp)


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

chicken_distance = [[] for _ in range(len(house))]


for i in range(len(house)):
    house_x, house_y = house[i]
    for j in range(len(chicken)):
        chicken_x, chicken_y = chicken[j]
        chicken_distance[i].append((calculate(house_x, house_y, chicken_x, chicken_y), j))
    chicken_distance[i].sort()


answer = 1000000

chicken_numlist = [i for i in range(len(chicken))]

#https://yaneodoo2.tistory.com/entry/
for k in combinations(chicken_numlist, M):
    solve(k)
print(answer)