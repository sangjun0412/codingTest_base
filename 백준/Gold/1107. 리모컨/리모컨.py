import sys
input = sys.stdin.readline
target = int(input())
n = int(input())
break_num= list(map(int, input().split()))

min_count = abs(100 - target)

for nums in range(1000001):
    nums = str(nums)
    
    for j in range(len(nums)):
        if int(nums[j]) in break_num:
            break

        elif j == len(nums) - 1:
            min_count = min(min_count, abs(int(nums) - target) + len(nums))#(min_count,현재채널에서 목표채널로 가기위한 버튼 클릭 횟수)

print(min_count)