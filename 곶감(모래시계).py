n = int(input())
num_list = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

dc = [-1, 1]

for _ in range(m):
    h, t, k = map(int, input().split())
    if t == 0:
        for _ in range(k):
            num_list[h - 1].append(num_list[h - 1].pop(0))
    else:
        for _ in range(k):
            num_list[h-1].insert(0, num_list[h-1].pop())

s = 0
e = n
res = 0
for i in range(n):
    for j in range(s, e):
        res += num_list[i][j]
    if i < n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(res)