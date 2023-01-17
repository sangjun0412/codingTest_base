"""
국가 예산의 총액은 미리 정해져 있어서, 모든 예산요청을 배정할수 없다.
가능한 최대의 총예산을 배정
모든 요청이 배정될수 있는 경우네는 요청한 그대로 배정
X -->  특정한 정수 상한액을 계산하여, 그 이상인 예산요청에는 모두상한액을 배정한다. 상한액 이하의 예산요청에 대해서는 요청하는 금액을 그대로
배정
"""

n = int(input()) # 지방의 개수
nl = list(map(int, input().split()))
budget = int(input())
start = 0
end = max(nl)

res = 0


while start <= end:
    mid = (start + end)//2
    tmp = 0
    for x in nl:
        tmp += min(x, mid)
    if budget < tmp:
        end = mid - 1
    else:
        start = mid + 1

print(end)