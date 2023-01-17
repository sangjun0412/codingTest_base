n = int(input())
num_list = [list(map(int, input().split())) for _ in range(n)]

max = -21700000

for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):  # 세로
        sum1 += num_list[j][i]
        sum2 += num_list[i][j]
    if max < sum1:
        max = sum1
    if max < sum2:
        max = sum2

tmp = 0
tmp2 = 0
for i in range(n):
    tmp += num_list[i][i]
    tmp2 += num_list[-1-i][-1-i]
if max < tmp:
    max = tmp
if max < tmp2:
    max = tmp2
print(max)