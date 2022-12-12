def dfs(v):
    if v > 7:
        return
    else:
        print(v)
        dfs(v*2)
        dfs(v*2 + 1)
    
dfs(1)
