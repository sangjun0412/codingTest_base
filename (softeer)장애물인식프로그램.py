import sys
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
dx =[0,0,1,-1]
dy =[1,-1,0,0]

def dfs(x,y):
    global max_num
    if x < 0 or x>=n or y<0 or y >= n:
        return
    else:
        if graph[x][y] == 1:
            graph[x][y] = 0
            max_num.append(1)
            dfs(x,y+1)
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y -1)
            return True
    return False
cnt = 0
res = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt += 1
            max_num = []
            dfs(i,j)
            res.append(len(max_num))

print(cnt)
res.sort()
for x in res:
    print(x)
