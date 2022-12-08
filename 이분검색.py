n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

low = 0
high = n - 1
res = 0
while low <= high:
    mid = int((low + high)/2)
    if m == num_list[mid]:
        res = mid
        break
    elif m < num_list[mid]:
        high = mid - 1
    elif m > num_list[mid]:
        low = mid + 1
print(res + 1)
