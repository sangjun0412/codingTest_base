n = int(input())
score_list = list(map(int, input().split()))
avg = round(sum(score_list)/n)
min = 2147000000
for idx, x in enumerate(score_list):
    tmp = abs(x - avg)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1
print(avg, res)
