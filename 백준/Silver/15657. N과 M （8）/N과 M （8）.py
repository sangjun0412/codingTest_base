
n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
visit = [False] * n
out = []


def function(start):
    global out

    if len(out) == m:
        print(' '.join(map(str, out)))
        return

    for i in range(start, n):
        out.append(num_list[i])
        function(i)
        out.pop()


function(0)