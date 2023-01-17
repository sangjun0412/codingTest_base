"""
num_list가 주어지고 두 개의 합이 0과 가장 가깝게 되는 num_list 값 2가지를 구하라
num_list가 오름차순으로 주어지고, 이 수들 모두 1억이 넘음 -> 투포인터를 활용하여 시간초과를 방지하여야 한다.
그렇다는건 투포인터를 하였을때 두개의 합이 0보다 크면, end 값을 줄이고 두개의 합이 0보다 작으면, start값을 하나 늘린다
근데 그 전 값보다 0과 가까이 가지 않는다면 그 전 값들을 저장해두고 그다음 인덱스로 넘어가 투포인터 작동을 계속해서 하고
가장 0과 가까이 가는 값을 구한다.
"""
n = int(input())
nl = list(map(int, input().split()))
start = 0
end = n - 1
res_min = 2147000000
res_l = 0
res_r = 0
while start < end:
    tmp = nl[start] + nl[end]
    if abs(tmp) < res_min:
        res_r = end
        res_l = start
        res_min = abs(tmp)
    if tmp > 0:
        end -= 1
    elif tmp < 0:
        start += 1
    else:
        break
print(nl[res_l], nl[res_r])