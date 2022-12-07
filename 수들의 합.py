n, m = map(int, input().split())
num_list = list(map(int, input().split()))
size = len(num_list)
# cnt = 0
# for i in range(size):
#     tmp = num_list[i]
#     if tmp == m:
#         cnt += 1
#     if tmp > m:
#         continue
#     else:
#         for j in range(i + 1, size):
#             tmp += num_list[j]
#             if tmp == m:
#                 cnt += 1
#                 break
#             elif tmp > m:
#                 break
# print(cnt)
# 시간초과 남
cnt = 0
lt = 0
rt = 1
tot = num_list[0]
while True:
    if tot < m:
        if rt < n:
            tot += num_list[rt]
            rt +=1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= num_list[lt]
        lt += 1
    else:
        tot -= num_list[lt]
        lt += 1
print(cnt)