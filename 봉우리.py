n = int(input())
num_list = [[0] * (n + 2) for _ in range(n + 2)]
tmp_list = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        num_list[i+1][j+1]=tmp_list[i][j]

res = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if all(num_list[i][j] > num_list[i+dx[k]][i+dy[k]] for k in range(4)):
            res += 1

print(res)