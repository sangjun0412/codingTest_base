"""
자기가 좋아하는 초밥을 골라서 먹음
초밥의 종류를 번호로 표현
같은 종류의 초밥이 존재할수 있음

- k개의 접시를 연속으로 먹으면 할인
- 위 조건을 만족할 시 초밥 쿠폰을 제공
- 위 행사를 참여하며 가능한 다양한 종류의 초밥을 먹음

- 회전 초밥음식점의 벨트 상태, 메뉴에 있는 초바븨 가짓수, 연속해서 먹는 접시의 개수, 쿠폰 번호 순으로 조건이 주어짐
- 손님이 먹을 수 있는 초밥 가짓수의 최댓값을 구함
"""

n, d, k, c = map(int, input().split()) # 초밥벨트의 접시수, 초밥의 가짓수, 연속해서 먹는 접시의 수, 쿠폰 번호
nl = [int(input()) for _ in range(n)]
# 두번째로 생각한건 고정된 크기로 되어있으니까 슬라이딩 윈도우를 한다.
# nl을 두번 더하는게 구린거 같아서 원형리스트를 구현하고자 한다.
# 그리고 체크할때 체크리스트로 하였는데,이것도 구린거 같아서 set으로 하겠다.
res =set()
start = 0
end = k - 1
plates = []

while start < n:
    if end >= n:
        end -= n # n보다 커지면 다시 맨 앞으로 가야되니까
    if end < start:
        plates = nl[start:] + nl[:end + 1]
    else:
        plates = nl[start:end + 1]
    tmp = set(plates)
    if c not in tmp:
        tmp.add(c)
    if len(res) < len(tmp):
        res = tmp
    start += 1
    end += 1
print(len(res))




# 시간초과난듯
# nl = nl + nl
# # 접시수가 30000까지고, 연속해서 먹어야 되는 경우가 3000까지 있으니까, dfs는 아닌듯
# # 그래서 맨처음 접시부터 체크를 함 연속해서 먹을수 있는 개수를 global 변수 res로 해서 쿠폰번호가 들어있지 않다면 +1 까지 해서 res에 계속 갱신
# # 근데 num list의 마지막에 다다를 수록 체크를 맨앞까지 해야되니까, num_list를 두배로하고 맨마지막까지 체크해보도록 하겠다.
#
#
# def check(now_plate):
#     ch = [0] * (d + 1)
#     now_cnt = 0
#
#     for i in range(now_plate, len(nl)):
#         if now_cnt == k:
#             break
#         if ch[nl[i]] == 0:
#             now_cnt += 1
#             ch[nl[i]] = 1
#             # print(nl[i])
#         else:
#             break
#
#     if now_cnt == k:
#         if ch[c] == 0:
#             now_cnt = now_cnt + 1
#             return now_cnt
#         else:
#             return now_cnt
#     else:
#         return now_cnt
#
#
# res = -1 # 각 그릇 중에 가장 많이 최대의 종류를 하는 경우
#
# for i in range(n):
#     tmp = check(i)
#     if tmp == k + 1:
#         res = tmp
#         break
#     if tmp > res:
#         res = tmp
#
# print(res)