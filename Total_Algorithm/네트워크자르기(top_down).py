n = int(input())
dy = [0] * (n+1)

def DFS(len):
    if dy[len] > 0:
        return dy[len]
    if len == 1 or len == 2:
        return len
    else:
        dy[len] = DFS(len - 1) + DFS(len -2)
        return dy[len]
print(DFS(n))