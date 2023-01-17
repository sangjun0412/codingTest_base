"""
무게가 서로 다른 K개의 추
양팔저울을 한번만 이용 -> 원하는 물의 무게
주어진 모든추 무게의 합 -> S
이 모든 추의 조합을 정하고,
"""
# 더하거나 뺏을 때 나올 수 있는 1~ms 까지의 값을 구하기.
k = int(input())
nl = list(map(int, input().split()))
ms = sum(nl) # 추가 가질 수 있는 가장 큰 값
ch = list() # 가질 수 있는 경우의 수 체크

def dfs(depth, tt): #tt -> total
    if depth == k:
        if 0 < tt <= ms:
            ch.append(tt)
        return
    else:
        dfs(depth + 1, tt + nl[depth])
        dfs(depth + 1, tt - nl[depth])
        dfs(depth + 1, tt)
dfs(0,0)

print(ms - len(list(set(ch))))