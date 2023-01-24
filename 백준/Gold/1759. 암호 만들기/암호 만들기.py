
def dfs(depth, idx):
    if depth == L:
        모음의수, 자음의수 = 0, 0
        for i in range(L):
            if answer[i] in 모음:
                모음의수 += 1
            else:
                자음의수 += 1

        if 모음의수>=1 and 자음의수 >=2:
            print("".join(answer))
        return

    for i in range(idx, C):
        if not visit[i]:
            answer.append(nl[i])
            visit[i] = 1
            dfs(depth + 1, i + 1)
            answer.pop()
            visit[i] = 0

L, C = map(int, input().split())
nl = list(map(str, input().split()))
nl.sort()
모음 = ["a", "e", "i", "o", "u"]
answer = []
visit =[0 for i in range(C)]
dfs(0,0)