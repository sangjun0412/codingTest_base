n = int(input())
num_list = list(map(int, input().split()))

ch = 1
res = 0
for i in num_list:
    if i == 0:
        ch = 1
    else:
        res += i * ch
        ch += 1

print(res)