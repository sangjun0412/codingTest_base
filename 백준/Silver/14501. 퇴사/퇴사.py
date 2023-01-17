N = int(input())
T = [0 for i in range(N + 1)]
P = [0 for i in range(N + 1)]

for i in range(N):
    a, b = map(int, input().split())
    T[i] = a
    P[i] = b

tmp = [0 for i in range(N + 1)]

for i in range(N-1, -1, -1):
    if T[i] + i <= N:
        tmp[i] = max(P[i] + tmp[i + T[i]], tmp[i + 1])
    else:
        tmp[i] = tmp[i + 1]

print(tmp[0], end='')