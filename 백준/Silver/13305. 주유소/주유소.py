n = int(input())
road = list(map(int,input().split()))
oil = list(map(int, input().split()))
oil.pop()
i = 0
min_oil = 214700000
res = 0
while True:
    if i == len(road):
        break
    else:
        if min_oil > oil[i]:
            min_oil = oil[i]
        res += min_oil * road[i]
        i += 1
print(res)