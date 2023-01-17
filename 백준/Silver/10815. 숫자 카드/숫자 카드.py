import sys

n = int(input())
list1 = list(map(int, sys.stdin.readline().split()))
m = int(input())
list2 = list(map(int, sys.stdin.readline().split()))

list1.sort()


def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for i in list2:
    result = binary_search(list1, i, 0, n - 1)
    if result != None:
        print(1, end=' ')
    else:
        print(0, end=' ')
