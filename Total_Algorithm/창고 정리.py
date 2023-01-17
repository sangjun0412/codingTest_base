L = int(input())
num_list = list(map(int, input().split()))
m = int(input())

num_list.sort()

for i in range(m):
    num_list[-1] -= 1
    num_list[0] += 1
    num_list.sort()

print(num_list[-1] - num_list[0])