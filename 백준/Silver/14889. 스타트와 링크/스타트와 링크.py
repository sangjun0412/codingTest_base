from itertools import combinations as cb

N = int(input())
graph = [list(map(int, input().split())) for i in range(N)]
min_val = 100
num_list = [i for i in range(0, N)]

def scoring(num_list_half):
    global min_val, num_list
    tmp = 0
    tmp2 = 0
    compare_list = []

    for i in num_list:
        if i not in num_list_half:
            compare_list.append(i)

    for i in num_list_half:
        for j in num_list_half:
            if i != j:
                tmp += graph[i][j] + graph[j][i]

    for i in compare_list:
        for j in compare_list:
            if i != j:
                tmp2 += graph[i][j] + graph[j][i]
    if tmp - tmp2 >= 0:
        min_val = min(tmp - tmp2, min_val)
    if tmp2 - tmp >= 0:
        min_val = min(tmp2 - tmp, min_val)

for i in cb(num_list, int(N / 2)):
    scoring(i)


print(int(min_val / 2))