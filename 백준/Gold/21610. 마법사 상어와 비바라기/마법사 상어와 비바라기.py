N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 초기 구름 위치 설정
clouds = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]

# 좌표 이동 설정
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
for _ in range(M):  # M번 반복
    d, s = map(int, input().split())

    # 구름 이동
    move_clouds = []
    for cloud_idx in range(len(clouds)):
        cloud_x, cloud_y = clouds[cloud_idx]
        # N을 더해 음의 좌표 처리, N나머지 연산으로 N보다 큰 좌표 처리
        next_cloud_x = (N + cloud_x + (dx[d - 1] * s)) % N
        next_cloud_y = (N + cloud_y + (dy[d - 1] * s)) % N

        move_clouds.append((next_cloud_x, next_cloud_y))  # 구름이 이동한 좌표를 리스트에 추가

    # 구름의 위치를 확인해주기 위한 N*N 행렬
    is_cloud = [[False] * N for _ in range(N)]
    # 구름의 위치에 따라 물 추가, 구름 위치 표기
    for mv_x, mv_y in move_clouds:
        A[mv_x][mv_y] += 1
        is_cloud[mv_x][mv_y] = True

    # 대각선 위치를 탐색해주기 위한 좌표 이동 인덱스 설정
    find_directions = [1, 3, 5, 7]
    # 구름의 대각선 위치를 검사하여 물 복사 버그
    for mv_x, mv_y in move_clouds:
        is_rain_count = 0
        # 대각선 칸에 물이 있는 칸이 몇 개 인지 세기
        for fd in find_directions:
            find_x, find_y = mv_x + dx[fd], mv_y + dy[fd]

            # 범위 밖인 경우 제외
            if not 0 <= find_x < N or not 0 <= find_y < N:
                continue
            # 물이 없는 경우 제외
            if A[find_x][find_y] == 0:
                continue

            is_rain_count += 1

        # 물이 있는 만큼 물 추가
        A[mv_x][mv_y] += is_rain_count

    # 새 구름 생성
    clouds = []
    for i in range(N):
        for j in range(N):
            # 물 양이 1이하이면 제외
            if A[i][j] <= 1:
                continue

            # 위에서 이동한 구름 위치가 아닌 경우, 구름 생성 및 물 양-2
            if not is_cloud[i][j]:
                clouds.append((i, j))
                A[i][j] -= 2

# 2차원 행렬 > 1차원 행렬 > sum 전체 합 계산, 출력
print(sum(sum(A, [])))
