tc = int(input())

for t in range(1, tc + 1):
    N = int(input())
    nl = [list(map(int, input().split())) for _ in range(N)]
    arr_90 = [[0 for _ in range(N)] for _ in range(N)]
    arr_180 = [[0 for _ in range(N)] for _ in range(N)]
    arr_270 = [[0 for _ in range(N)] for _ in range(N)]

    # arr 행렬 90도 회전
    for i in range(N):
        for j in range(N):
            arr_90[i][j] = nl[N - 1 - j][i]

    # arr_90 행렬을 90도 회전하면 arr_180 행렬
    for i in range(N):
        for j in range(N):
            arr_180[i][j] = arr_90[N - 1 - j][i]

    # arr_180 행렬을 90도 회전하면 arr_270 행렬
    for i in range(N):
        for j in range(N):
            arr_270[i][j] = arr_180[N - 1 - j][i]

    print(f'#{t}')
    for i in range(N):
        for a in range(N):
            print(arr_90[i][a], end='')
        print(end=' ')
        for b in range(N):
            print(arr_180[i][b], end='')
        print(end=' ')
        for c in range(N):
            print(arr_270[i][c], end='')
        print()