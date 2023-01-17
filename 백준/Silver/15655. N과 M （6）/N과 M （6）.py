n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
visit = [0] * n
out = []


def function(start):
    if len(out) == m:
        print(*out)
        return

    for i in range(start, n):
        if not visit[i]:
            visit[i] = True
            out.append(num_list[i])
            function(i + 1)
            out.pop()
            visit[i] = False


function(0)
