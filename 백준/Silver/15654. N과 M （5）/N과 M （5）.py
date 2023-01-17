
n, m = map(int, input().split())

num_list = list(map(int, input().split()))
num_list.sort()
out = []
visit = [False] * n


def backtracking(start):
    global out
    if start == m:
        print(' '.join(map(str, out)))
        return

    for i in range(n):
        if not visit[i]:
            visit[i] = True
            out.append(num_list[i])
            backtracking(start+1)
            out.pop()
            visit[i] = False


backtracking(0)
