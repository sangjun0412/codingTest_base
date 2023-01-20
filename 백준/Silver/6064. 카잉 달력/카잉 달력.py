"""
x< m이면 x = x+1 -> x == m -> x = 1
y <n이면 y = y+1 -> y == n -> y = 1
m:n이 달력의 마지막 해
그러면 x:y는 몇번째 해인가??


"""
for _ in range(int(input())):
    m,n,x,y = map(int,input().split())
    flag = 1
    while (x<=m*n):
        if x%n == y %n:
            print(x)
            flag = 0
            break
        x += m
    if flag:
        print(-1)
# 시간 초과
# tc = int(input())
# 
# def check(m, n, x, y, sx, sy):
#     global cnt
#     while True:
#         if sx == m and sy == n:
#             print(-1)
#             return
#         if sx > m:
#             sx = 1
#         if sy > n:
#             sy = 1
#         sx += 1
#         sy += 1
#         cnt += 1
# 
#         if sx == x and sy == y:
#             print(cnt)
#             return
# 
# 
# for t in range(tc):
#     m, n, x, y = map(int, input().split())
#     cnt = 0
#     check(m, n, x, y, 0, 0)
