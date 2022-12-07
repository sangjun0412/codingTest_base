n = int(input())
num_list = list(map(int, input().split()))
m = int(input())
num_list2 = list(map(int, input().split()))
p1 = p2 = 0
c = []

while p1 < n and p2 < m:
    if num_list[p1] <= num_list2[p2]:
        c.append(num_list[p1])
        p1 += 1
    else:
        c.append(num_list2[p2])
        p2 += 1

if p1 < n:
    c = c+ num_list[p1:]
if p2 < m:
    c = c+ num_list2[p2:]
print(*c)
